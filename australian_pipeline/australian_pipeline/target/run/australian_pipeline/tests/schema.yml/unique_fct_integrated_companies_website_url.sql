select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    website_url as unique_field,
    count(*) as n_records

from "company_data"."public"."fct_integrated_companies"
where website_url is not null
group by website_url
having count(*) > 1



      
    ) dbt_internal_test