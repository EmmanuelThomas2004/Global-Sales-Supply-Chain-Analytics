# Snowflake SQL Analysis

This folder contains the SQL scripts used to configure the Snowflake environment, load the cleaned dataset, create analytical views, and prepare dashboard-ready data for the Global Sales & Supply Chain Analytics project.

## SQL Files

### `00_setup.sql`
Sets up the Snowflake environment required for the project, including the warehouse, database, schema, stage, and CSV file format.

### `01_load data.sql`
Loads the cleaned supply chain dataset into the Snowflake table and supports validation of the loaded data.

### `1_executive_analysis.sql`
Creates analytical views and KPI calculations used for the Global Supply Chain Performance Dashboard.

### `2_sales_profit_analysis.sql`
Contains SQL analysis for sales and profitability, including category performance, product performance, and market-level sales and profit.

### `3_customer_market_analysis.sql`
Creates analytical views for customer segments, top customers, country-level sales, market performance, and customer KPIs.

### `4_supply_chain_delivery_analysis.sql`
Analyzes delivery and supply chain performance, including late-delivery rates, shipping delays, shipping modes, delivery risk, and actual versus scheduled shipping time.

## SQL Techniques Used

- Aggregate functions (`SUM`, `AVG`, `COUNT`)
- `GROUP BY`
- `CASE WHEN`
- Subqueries
- `COUNT(DISTINCT)`
- Window functions
- `DENSE_RANK()`
- `QUALIFY`
- `NULLIF`
- Analytical views using `CREATE OR REPLACE VIEW`
- Sorting and Top-N analysis

## Analytics Workflow

**Snowflake Setup → Data Loading → SQL Views → KPI & Business Analysis → Power BI Dashboards**

The SQL layer transforms the cleaned transactional data into structured analytical outputs that are consumed by Power BI for visualization and business reporting.
