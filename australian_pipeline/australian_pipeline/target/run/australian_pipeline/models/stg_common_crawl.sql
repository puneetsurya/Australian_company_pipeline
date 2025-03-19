
  create view "company_data"."public"."stg_common_crawl__dbt_tmp"
    
    
  as (
    
SELECT website_url, company_name, crawl_date FROM "company_data"."public"."common_crawl_websites";
  );