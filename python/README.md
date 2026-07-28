# Python Data Cleaning

This folder contains the Python script used to clean and preprocess the raw supply chain dataset before loading it into Snowflake.

## Key Tasks

- Identified and handled missing values
- Checked and removed duplicate records
- Validated and corrected data types
- Processed date and timestamp columns
- Removed unnecessary columns
- Created analysis-ready fields
- Exported the cleaned dataset for Snowflake ingestion

## File

- `data_cleaning.py` — Python/Pandas script used for data cleaning and preprocessing

## Output

The cleaned dataset contains **180,519 records** and is used as the primary input for the Snowflake analytics workflow.
