# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 18:58:24 2025

@author: Acer
"""
import warcio
import requests
import psycopg2
import datetime
import re
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry
import time
import urllib3

def extract_common_crawl_data(warc_paths_file, db_params):
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        processed_warc_count = 0

        with open(warc_paths_file, 'r') as f:
            for warc_path in f:
                warc_path = warc_path.strip()
                try:
                    session = requests.Session()
                    retry = Retry(connect=3, backoff_factor=0.5)
                    adapter = HTTPAdapter(max_retries=retry)
                    session.mount('http://', adapter)
                    session.mount('https://', adapter)

                    try:
                        with session.get(f"https://data.commoncrawl.org/{warc_path}", stream=True, timeout=20) as response:
                            response.raise_for_status()
                            try:
                                for record in warcio.ArchiveIterator(response.raw):
                                    if record.rec_type == 'response':
                                        url = record.rec_headers.get_header('WARC-Target-URI')
                                        if "au" in url:
                                            try:
                                                with session.get(url, timeout=20) as response_content:
                                                    response_content.raise_for_status()
                                                    company_name = extract_company_name_from_html(response_content.text)
                                                    crawl_date = datetime.date.today()
                                                    cur.execute(
                                                        "INSERT INTO common_crawl_websites (website_url, company_name, crawl_date) VALUES (%s, %s, %s) ON CONFLICT (website_url) DO NOTHING;",
                                                        (url, company_name, crawl_date),
                                                    )
                                            except requests.exceptions.RequestException as e:
                                                print(f"Error fetching {url}: {e}")
                            except urllib3.exceptions.ProtocolError as e:
                                print(f"Error processing WARC file {warc_path}: {e}")
                            except warcio.exceptions.ArchiveLoadFailed as e:
                                print(f"Error processing WARC file {warc_path}: {e}")
                    except requests.exceptions.RequestException as e:
                        print(f"Error downloading WARC file {warc_path}: {e}")

                    processed_warc_count += 1
                    if processed_warc_count >= 10:
                        break #stop processing after 10 warc files.
                    time.sleep(1)

                except Exception as e:
                    print(f"General error processing warc file {warc_path}: {e}")

        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Database error: {e}")

def extract_company_name_from_html(html_text):
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        title = soup.find('title')
        if title:
            return title.text.strip()
        copyright_notice = soup.find(string=re.compile(r'©|\(c\)'))
        if copyright_notice:
            match = re.search(r'©|\(c\) (.*)', copyright_notice)
            if match:
                return match.group(1).strip()

        return "Company Name Not Found"

    except Exception as e:
        print(f"Error extracting company name: {e}")
        return "Company Name Extraction Error"

db_params = {
    "host": "localhost",
    "database": "company_data",
    "user": "postgres",
    "password": "punurocks007",
}
extract_common_crawl_data(r"C:\Users\Acer\Downloads\warc.paths (1)", db_params)