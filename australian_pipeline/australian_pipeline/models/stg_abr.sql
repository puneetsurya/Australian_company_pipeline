{{ config(materialized='view') }}
SELECT abn, entity_type, legal_name, company_name, trading_name, state, postcode FROM {{ source('raw_data', 'abr_companies') }};