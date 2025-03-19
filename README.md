
# Australian Company Data Pipeline

This repository contains the files for the Australian Company Data Pipeline assignment.

## Instructions

### Prerequisites

* PostgreSQL installed and running.
* Python 3.x installed.
* dbt installed (`pip install dbt-postgres`).
* Required Python libraries installed (`pip install warcio requests psycopg2 beautifulsoup4`).
* dbt setup with correct profile to connect to the database.

### Setup

1.  **Clone the Repository:**
    ```bash
    git clone [repository_url]
    cd Australian-Company-Data-Pipeline
    ```
2.  **Create Database:**
    * Run the SQL script `database_schema.sql` to create the database and tables.
3.  **Run Python Scripts:**
    * Execute `common_crawl_extraction.py` and `abr_extraction.py` to populate the database.
4.  **Configure dbt:**
    * Ensure your `profiles.yml` file is configured correctly for your PostgreSQL connection.
5.  **Run dbt:**
    ```bash
    cd dbt_project
    dbt run
    dbt test
    ```
6.  **Run Data Quality Check:**
    * Execute `data_quality_check.py`.

### Files

* `common_crawl_extraction.py`: Python script for extracting data from Common Crawl.
* `abr_extraction.py`: Python script for extracting data from ABR.
* `data_quality_check.py`: Python script for data quality checks.
* `dbt_project/`: dbt project directory.
* `database_schema.sql`: SQL script for database schema.
* `README.md`: This file.

### Output
Screenshots of the database tables and query results are also included in the repository.
