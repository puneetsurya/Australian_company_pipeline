{{ config(materialized='view') }}
SELECT cc.website_url, abr.abn, cc.company_name AS common_crawl_company_name, abr.company_name AS abr_company_name, abr.entity_type, abr.legal_name, abr.trading_name, abr.state, abr.postcode, cc.crawl_date
FROM {{ ref('stg_common_crawl') }} cc
LEFT JOIN {{ ref('stg_abr') }} abr ON LOWER(cc.company_name) = LOWER(abr.company_name);