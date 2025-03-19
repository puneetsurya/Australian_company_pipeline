select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      select * from "company_data"."public"."fct_integrated_companies" where abn is null and common_crawl_company_name != 'Company Name Not Found'
      
    ) dbt_internal_test