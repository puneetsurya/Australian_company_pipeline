select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select website_url
from "company_data"."public"."fct_integrated_companies"
where website_url is null



      
    ) dbt_internal_test