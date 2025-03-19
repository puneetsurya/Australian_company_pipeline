
  create view "company_data"."public"."stg_abr__dbt_tmp"
    
    
  as (
    
SELECT abn, entity_type, legal_name, company_name, trading_name, state, postcode FROM "company_data"."public"."abr_companies";
  );