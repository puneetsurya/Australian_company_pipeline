# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 19:01:01 2025

@author: Acer
"""
import xml.etree.ElementTree as ET
import psycopg2

def extract_abr_data(xml_file, db_params):
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for record in root.findall(".//searchResultsRecord"):
            abn = record.find(".//ABN").text
            entity_type = record.find(".//entityType").text
            legal_name = record.find(".//legalName").text
            business_name = record.find(".//businessName").text
            trading_name = record.find(".//tradingName").text
            state = record.find(".//state").text
            postcode = record.find(".//postcode").text

            cur.execute(
                """
                INSERT INTO abr_companies (abn, entity_type, legal_name, company_name, trading_name, state, postcode)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (abn) DO NOTHING;
                """,
                (abn, entity_type, legal_name, business_name, trading_name, state, postcode),
            )
        conn.commit()
        cur.close()
        conn.close()
    except (ET.ParseError, psycopg2.Error) as e:
        print(f"Error processing ABR data: {e}")

db_params = {
    "host": "localhost",
    "database": "company_data",
    "user": "postgres",
    "password": "punurocks007", #Replace with your password.
}
extract_abr_data(r"C:\Users\Acer\Downloads\20250305_Public01.xml", db_params) #Replace with your path.