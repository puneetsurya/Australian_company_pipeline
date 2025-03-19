-- Create common_crawl_websites table
CREATE TABLE common_crawl_websites (
    website_url VARCHAR PRIMARY KEY,
    company_name VARCHAR,
    crawl_date DATE
);

-- Create abr_companies table
CREATE TABLE abr_companies (
    abn VARCHAR PRIMARY KEY,
    entity_type VARCHAR,
    legal_name VARCHAR,
    company_name VARCHAR,
    trading_name VARCHAR,
    state VARCHAR,
    postcode VARCHAR
);

-- Create integrated_companies table
CREATE TABLE integrated_companies (
    website_url VARCHAR PRIMARY KEY,
    abn VARCHAR,
    common_crawl_company_name VARCHAR,
    abr_company_name VARCHAR,
    entity_type VARCHAR,
    legal_name VARCHAR,
    trading_name VARCHAR,
    state VARCHAR,
    postcode VARCHAR,
    crawl_date DATE,
    FOREIGN KEY (abn) REFERENCES abr_companies(abn),
    FOREIGN KEY (website_url) REFERENCES common_crawl_websites(website_url)
);

--Create Reader Role
CREATE ROLE reader WITH LOGIN;
GRANT CONNECT ON DATABASE company_data TO reader;
GRANT USAGE ON SCHEMA public TO reader;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO reader;