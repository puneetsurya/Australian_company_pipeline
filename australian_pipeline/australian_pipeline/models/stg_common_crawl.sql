{{ config(materialized='view') }}
SELECT website_url, company_name, crawl_date FROM {{ source('raw_data', 'common_crawl_websites') }};