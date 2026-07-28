# Snowflake Data Warehouse

This folder contains supporting documentation and visual evidence of the Snowflake implementation used in the Global Sales & Supply Chain Analytics project.

Snowflake was used as the cloud data warehouse to store the cleaned dataset and support SQL-based analytical processing.

## Snowflake Implementation

The project includes:

- Virtual warehouse configuration
- Database and schema creation
- Stage creation for data ingestion
- CSV file format configuration
- Loading the cleaned dataset into Snowflake
- Validation of loaded records
- Creation of analytical SQL views
- KPI calculations and aggregations
- Query execution for dashboard-ready datasets

## Data Warehouse Structure

The Snowflake environment was configured using:

- **Warehouse:** `DATACO_WH`
- **Database:** `DATACO_DB`
- **Schema:** `SUPPLY_CHAIN`
- **Stage:** `DATACO_STAGE`
- **File Format:** `CSV_FORMAT`
- **Primary Table:** `DATACO_RAW`

The final Snowflake table contains **180,519 records** used for downstream analysis.

## Screenshot

- `snowflake_query_execution.png` — Demonstrates SQL query execution and analytical processing within Snowflake.

## SQL Analysis

The SQL scripts used to configure Snowflake, load the dataset, create analytical views, and generate dashboard-ready results are available in the `sql` folder.

## Workflow

**Cleaned Dataset → Snowflake Stage → Data Warehouse → SQL Views → Power BI Dashboards**
