import pandas as pd
pd.set_option('display.max_columns', None)
dataco_path = r"C:\Users\emman\OneDrive\projects\DataCoSupplyChainDataset.csv"
logs_path = r"C:\Users\emman\OneDrive\projects\tokenized_access_logs.csv"
df = pd.read_csv(dataco_path, encoding='latin1')
logs = pd.read_csv(logs_path)
print("DataCo Shape:", df.shape)
print("Access Logs Shape:", logs.shape)
print("\nDataCo Dataset:")
print(df.head())
print("\nAccess Logs Dataset:")
print(logs.head())
#INFO
df.info()
logs.info()
#missing value
print("df null value")
print(df.isnull().sum())
print("logsnull value")
print(logs.isnull().sum())
#duplicate audit
print("df totl duplicate")
print(df.duplicated().sum())
print("logs duplicate")
print(logs.duplicated().sum())
print("each row no of dup")
a=logs.apply(lambda x: x.duplicated().sum())
print(a)
b=df.apply(lambda x: x.duplicated().sum())
print(b)
R = logs[logs.duplicated(keep=False)].head(20)
print(R)
print("ustomer emial unique")
print(df["Customer Email"].nunique())
print("cutomers Customer Password")
print(df["Customer Password"].nunique())
print(df.head(4))
df = df.drop(columns= ["Customer Email","Customer Password","Product Image","Product Description"])
print(df.shape)
totalmissing = df["Order Zipcode"].isna().sum()
print(totalmissing)
permissing = totalmissing /180519*100
print(permissing)
df = df.drop(["Order Zipcode"],axis = 1)
print(df.shape)
ab = df.apply(lambda x: x.isnull().sum())
print(ab)
cd = logs.apply(lambda x: x.isnull().sum())
print(cd)
print("Rows with missing Customer Lname:")
print(df[df["Customer Lname"].isna()])
print(df[df["Customer Zipcode"].isna()])
df["Customer Lname"] = df["Customer Lname"].fillna("Unknown")
df["order date (DateOrders)"] = pd.to_datetime(df["order date (DateOrders)"])
df["shipping date (DateOrders)"] = pd.to_datetime(df["shipping date (DateOrders)"])
ef = logs.apply(lambda x: x.isnull().sum())
print(ef)
logs["Date"] = pd.to_datetime(logs["Date"])
logs.info()
df.info()
columns = [
    "Days for shipping (real)","Days for shipment (scheduled)","Benefit per order","Sales per customer","Order Item Discount",
    "Order Item Discount Rate","Order Item Product Price","Order Item Profit Ratio","Order Item Quantity","Sales","Order Item Total",
    "Order Profit Per Order","Product Price"
]
print(df[columns].min())
print(df[columns].max())
print("Order Profit Per Order smallest")
print(df.nsmallest(10, "Order Profit Per Order"))
print("Order Profit Per Order max")
print(df.nlargest(10, "Order Profit Per Order"))

categorical_columns = [
    "Delivery Status",
    "Order Status",
    "Shipping Mode",
    "Market",
    "Customer Segment",
    "Department Name",
    "Category Name"
    ]
for col in categorical_columns:
    print(f"\n{'='*50}")
    print(f"column: {col}")
    print(f"uniquevalues:{df[col].nunique()}")
    print(df[col].value_counts())
product_check = df.groupby("Product Card Id")["Product Name"].nunique().sort_values(ascending=False)
print(product_check)
category_check = df.groupby("Product Category Id")["Category Name"].nunique().sort_values(ascending=False)
print(category_check)
department_check  =df.groupby("Department Id")["Department Name"].nunique().sort_values(ascending=False)
print(department_check)
customer_check  = df.groupby("Customer Id")[["Customer Fname", "Customer Lname"]].nunique()
print(customer_check)
order_check = df.groupby("Order Id")["Customer Id"].nunique().sort_values(ascending=False)
print(order_check)
text_columns = [
    "Product Name",
    "Category Name",
    "Department Name",
    "Customer Fname",
    "Customer Lname"
]

for col in text_columns:
    df[col] = df[col].str.strip()
for col in text_columns:
    df[col] = df[col].str.title()
df.info()
df["Order Year"] = df["order date (DateOrders)"].dt.year
df["Order Month"] = df["order date (DateOrders)"].dt.month_name()
df["Order Quarter"] = df["order date (DateOrders)"].dt.quarter
df["Order Day"] = df["order date (DateOrders)"].dt.day_name()
df["Shipping Delay"] = df["Days for shipping (real)"]-df["Days for shipment (scheduled)"]
print("="*50)
print("Shape")
print(df.shape)

print("\n"+"="*50)
print("Missing Values")
print(df.isnull().sum())

print("\n"+"="*50)
print("Duplicate Rows")
print(df.duplicated().sum())

print("\n"+"="*50)
print("Data Types")
print(df.dtypes)

print("\n"+"="*50)
print("Feature Columns")

feature_columns = [
    "Order Year",
    "Order Month",
    "Order Quarter",
    "Order Day",
    "Shipping Delay"
]

print(df[feature_columns].head())
print(df["Customer Country"].unique())
df["Customer Country"] = df["Customer Country"].replace( "EE. UU.","United States")
print(df["Customer Country"].head(5))
df.to_csv(
    r"C:\Users\emman\OneDrive\projects\DataCo Supply Chain dataset project\DataCoSupplyChain_Cleaned.csv",
    index=False
)
import os

path = r"C:\Users\emman\OneDrive\projects\DataCo Supply Chain dataset project\DataCoSupplyChain_Cleaned.csv"

print(os.path.exists(path))

CREATE WAREHOUSE DATACO_WH
WITH
WAREHOUSE_SIZE = "X-SMALL"
AUTO_SUSPEND = 300
AUTO_RESUME = TRUE;

CREATE DATABASE DATACO_DB;
CREATE SCHEMA SUPPLY_CHAIN;
USE SCHEMA SUPPLY_CHAIN;
CREATE STAGE DATACO_STAGE;
CREATE FILE FORMAT CSV_FORMAT
TYPE = 'CSV'
FIELD_DELIMITER = ','
SKIP_HEADER = 1
FIELD_OPTIONALLY_ENCLOSED_BY = '"';

CREATE OR REPLACE TABLE DATACO_RAW (
    TYPE VARCHAR,
    DAYS_FOR_SHIPPING_REAL NUMBER,
    DAYS_FOR_SHIPMENT_SCHEDULED NUMBER,
    BENEFIT_PER_ORDER FLOAT,
    SALES_PER_CUSTOMER FLOAT,
    DELIVERY_STATUS VARCHAR,
    LATE_DELIVERY_RISK NUMBER,
   CATEGORY_ID NUMBER,CATEGORY_NAME VARCHAR,
    CUSTOMER_CITY VARCHAR,
    CUSTOMER_COUNTRY VARCHAR,
    CUSTOMER_FNAME VARCHAR,
    CUSTOMER_ID NUMBER,
    CUSTOMER_LNAME VARCHAR,
    CUSTOMER_SEGMENT VARCHAR,
    CUSTOMER_STATE VARCHAR,
    CUSTOMER_STREET VARCHAR,
    CUSTOMER_ZIPCODE FLOAT,
    DEPARTMENT_ID NUMBER,
    DEPARTMENT_NAME VARCHAR,

    LATITUDE FLOAT,
    LONGITUDE FLOAT,

    MARKET VARCHAR,

    ORDER_CITY VARCHAR,
    ORDER_COUNTRY VARCHAR,
    ORDER_CUSTOMER_ID NUMBER,

    ORDER_DATE TIMESTAMP,

    ORDER_ID NUMBER,

    ORDER_ITEM_CARDPROD_ID NUMBER,
    ORDER_ITEM_DISCOUNT FLOAT,
    ORDER_ITEM_DISCOUNT_RATE FLOAT,
    ORDER_ITEM_ID NUMBER,
    ORDER_ITEM_PRODUCT_PRICE FLOAT,
    ORDER_ITEM_PROFIT_RATIO FLOAT,
    ORDER_ITEM_QUANTITY NUMBER,

    SALES FLOAT,
    ORDER_ITEM_TOTAL FLOAT,
    ORDER_PROFIT_PER_ORDER FLOAT,

    ORDER_REGION VARCHAR,
    ORDER_STATE VARCHAR,
    ORDER_STATUS VARCHAR,

    PRODUCT_CARD_ID NUMBER,
    PRODUCT_CATEGORY_ID NUMBER,
    PRODUCT_NAME VARCHAR,
    PRODUCT_PRICE FLOAT,
    PRODUCT_STATUS NUMBER,

    SHIPPING_DATE TIMESTAMP,
    SHIPPING_MODE VARCHAR,

    ORDER_YEAR NUMBER,
    ORDER_MONTH VARCHAR,
    ORDER_QUARTER NUMBER,
    ORDER_DAY VARCHAR,

    SHIPPING_DELAY NUMBER

);

COPY INTO DATACO_RAW FROM @DATACO_STAGE FILE_FORMAT = (FORMAT_NAME = CSV_FORMAT);


CREATE OR REPLACE  VIEW VW_EXECUTIVE_KPIS AS
SELECT ROUND(SUM(SALES),2) AS TOTAL_SALES,
ROUND(SUM(ORDER_PROFIT_PER_ORDER),2) AS Total_Profit,
COUNT(DISTINCT ORDER_ID) AS TOTAL_ORDERS,
COUNT(DISTINCT CUSTOMER_ID) AS Total_Customers,
SUM(ORDER_ITEM_QUANTITY) AS Total_Quantity_Sold,
ROUND(SUM(SALES)/COUNT(DISTINCT ORDER_ID),2) AS AVG_ORDER_VALUE,
ROUND(SUM(ORDER_PROFIT_PER_ORDER)/COUNT(DISTINCT ORDER_ID),2) AS Average_Profit_per_Order,
ROUND(AVG(ORDER_ITEM_DISCOUNT_RATE),2) AS Average_Discount_Rate,
ROUND((SUM(ORDER_PROFIT_PER_ORDER)/SUM(SALES)) * 100,2) AS Profit_Margin_PERCENT
FROM DATACO_RAW;


CREATE OR REPLACE VIEW VW_SALES_TREND AS
SELECT
ORDER_YEAR,
ORDER_QUARTER,
ORDER_MONTH,
ROUND(SUM(SALES),2) AS TOTAL_SALES,
ROUND(SUM(ORDER_PROFIT_PER_ORDER),2) AS Total_Profit,
COUNT(DISTINCT ORDER_ID) AS TOTAL_ORDERS,
SUM(ORDER_ITEM_QUANTITY) AS Total_Quantity_Sold
FROM DATACO_RAW GROUP BY ORDER_YEAR,ORDER_QUARTER,ORDER_MONTH;

CREATE OR REPLACE VIEW VW_CUSTOMER_ANALYSIS AS
SELECT
    CUSTOMER_ID,
    CUSTOMER_FNAME,
    CUSTOMER_LNAME,
    CUSTOMER_SEGMENT,
    MARKET,
    ROUND(SUM(SALES),2) AS TOTAL_SALES,
    ROUND(SUM(ORDER_PROFIT_PER_ORDER),2) AS TOTAL_PROFIT,
    COUNT(DISTINCT ORDER_ID) AS TOTAL_ORDERS,
    SUM(ORDER_ITEM_QUANTITY) AS TOTAL_QUANTITY_SOLD,
    ROUND(SUM(SALES)/COUNT(DISTINCT ORDER_ID),2) AS AVG_ORDER_VALUE
FROM DATACO_RAW
GROUP BY
    CUSTOMER_ID,
    CUSTOMER_FNAME,
    CUSTOMER_LNAME,
    CUSTOMER_SEGMENT,
    MARKET;




CREATE OR REPLACE VIEW VW_MARKET_ANALYSIS AS
SELECT MARKET,
ORDER_REGION,
ORDER_COUNTRY,
ROUND(SUM(SALES),2) AS TOTAL_SALES,
    ROUND(SUM(ORDER_PROFIT_PER_ORDER),2) AS TOTAL_PROFIT,
    COUNT(DISTINCT ORDER_ID) AS TOTAL_ORDERS,
    SUM(ORDER_ITEM_QUANTITY) AS TOTAL_QUANTITY_SOLD,
    ROUND(SUM(SALES)/COUNT(DISTINCT ORDER_ID),2) AS AVG_ORDER_VALUE
FROM DATACO_RAW
GROUP BY
MARKET,
ORDER_REGION,
ORDER_COUNTRY;



CREATE OR REPLACE VIEW VW_SHIPPING_ANALYSIS AS
SELECT SHIPPING_MODE,
ROUND(AVG(SHIPPING_DELAY),2)AS AVG_SHIPPING_DELAY,
DELIVERY_STATUS,
ROUND(SUM(SALES),2) AS TOTAL_SALES,
    ROUND(SUM(ORDER_PROFIT_PER_ORDER),2) AS TOTAL_PROFIT,
    COUNT(DISTINCT ORDER_ID) AS TOTAL_ORDERS,
SUM(CASE WHEN DELIVERY_STATUS = 'Late delivery' THEN 1 ELSE 0 END) AS LATE_DELIVERY_COUNT
FROM DATACO_RAW
 GROUP BY SHIPPING_MODE,DELIVERY_STATUS;



CREATE OR REPLACE VIEW VW_DISCOUNT_PROFIT_ANALYSIS AS
SELECT
ORDER_ITEM_DISCOUNT_RATE,
ROUND(SUM(SALES),2) AS TOTAL_SALES,
ROUND(SUM(ORDER_PROFIT_PER_ORDER),2) AS TOTAL_PROFIT,
COUNT(DISTINCT ORDER_ID) AS TOTAL_ORDERS,
SUM(ORDER_ITEM_QUANTITY) AS TOTAL_QUANTITY_SOLD
FROM DATACO_RAW GROUP BY ORDER_ITEM_DISCOUNT_RATE;

CREATE OR REPLACE VIEW VW_PRODUCT_PERFORMANCE AS
SELECT
    PRODUCT_NAME,
    CATEGORY_NAME,
    DEPARTMENT_NAME,
    ROUND(SUM(SALES),2) AS TOTAL_SALES,
    ROUND(SUM(ORDER_PROFIT_PER_ORDER),2) AS TOTAL_PROFIT,
    COUNT(DISTINCT ORDER_ID) AS TOTAL_ORDERS,
    SUM(ORDER_ITEM_QUANTITY) AS TOTAL_QUANTITY_SOLD,
    ROUND(AVG(ORDER_ITEM_DISCOUNT_RATE),2) AS AVERAGE_DISCOUNT_RATE
FROM DATACO_RAW
GROUP BY
    PRODUCT_NAME,
    CATEGORY_NAME,
    DEPARTMENT_NAME;


CREATE OR REPLACE VIEW VW_ORDER_ANALYSIS AS
SELECT
    ORDER_STATUS,
    ROUND(SUM(ORDER_PROFIT_PER_ORDER),2) AS TOTAL_PROFIT,
    COUNT(DISTINCT ORDER_ID) AS TOTAL_ORDERS,
    ROUND(SUM(SALES),2) AS TOTAL_SALES,
    SUM(ORDER_ITEM_QUANTITY) AS TOTAL_QUANTITY_SOLD,
    ROUND(SUM(SALES)/COUNT(DISTINCT ORDER_ID),2) AS AVG_ORDER_VALUE
FROM DATACO_RAW
GROUP BY
    ORDER_STATUS;


 TOP 10 Sales & Profit by Category
CREATE OR REPLACE VIEW VW_TOP10_CATEGORY_SALES_PROFIT AS
SELECT
    CATEGORY_NAME,
    SUM(SALES) AS TOTAL_SALES,
    SUM(ORDER_PROFIT_PER_ORDER) AS TOTAL_PROFIT,
    DENSE_RANK() OVER (ORDER BY SUM(SALES) DESC) AS SALES_RANK
FROM DATACO_RAW
GROUP BY CATEGORY_NAME
QUALIFY SALES_RANK <= 10;
   SELECT CATEGORY_NAME,SUM(SALES) AS TOTAL_SALES,
   SUM(ORDER_PROFIT_PER_ORDER) AS TOTAL_PROFIT,
   DENSE_RANK() OVER( ORDER BY SUM(SALES) DESC) AS RANK
   FROM DATACO_RAW GROUP BY CATEGORY_NAME
   QUALIFY   RANK <= 10 ORDER BY RANK;


Top 10 Products by Sales
CREATE OR REPLACE VIEW Top_10_Products_by_Sales AS
SELECT PRODUCT_NAME,SUM(SALES) AS TOTAL_SALES,DENSE_RANK() OVER(ORDER BY SUM(SALES) DESC) AS RANK FROM DATACO_RAW
GROUP BY PRODUCT_NAME QUALIFY RANK <= 10 ORDER BY RANK;



Top/Bottom Products by Profit
CREATE OR REPLACE VIEW Top_Bottom_Products_by_Profit AS
SELECT
SUM(ORDER_PROFIT_PER_ORDER) AS TOTAL_PROFIT,
PRODUCT_NAME,
DENSE_RANK() OVER(ORDER BY SUM(ORDER_PROFIT_PER_ORDER) DESC) AS TOP_5,
DENSE_RANK() OVER(ORDER BY SUM(ORDER_PROFIT_PER_ORDER) ASC) AS BOTTOM_5
FROM DATACO_RAW
GROUP BY PRODUCT_NAME QUALIFY TOP_5 <= 5 OR BOTTOM_5 <= 5;

SELECT * FROM Top_Bottom_Products_by_Profit;


Sales vs Profit by Market
CREATE OR REPLACE VIEW Sales_vs_Profit_by_Market AS
SELECT MARKET,
SUM(SALES) AS TOTAL_SALES,
SUM(ORDER_PROFIT_PER_ORDER) AS TOTAL_PROFIT
FROM DATACO_RAW
GROUP BY  MARKET
ORDER BY TOTAL_SALES DESC;







CREATE OR REPLACE VIEW Sales_by_Customer_Segment AS
SELECT
ROUND(SUM(SALES),2) AS TOTAL_SALES,
Customer_Segment
FROM DATACO_RAW
GROUP BY Customer_Segment;

CREATE OR REPLACE VIEW Profit_by_Customer_Segment AS
SELECT
ROUND(SUM(ORDER_PROFIT_PER_ORDER),2) AS TOTAL_PROFIT,
Customer_Segment
FROM
DATACO_RAW
GROUP BY
Customer_Segment;

CREATE OR REPLACE VIEW top_10_country_by_totalsales AS
SELECT
ROUND(SUM(SALES),2) AS TOTAL_SALES,
Order_Country,
DENSE_RANK() OVER(ORDER BY ROUND(SUM(SALES),2) DESC) as rank
FROM DATACO_RAW
GROUP BY
Order_Country qualify rank <= 10;


CREATE OR REPLACE VIEW top_10_customers_by_totalsales AS
SELECT
ROUND(SUM(SALES),2) AS TOTAL_SALES,
Customer_Id
FROM DATACO_RAW
GROUP BY Customer_Id
ORDER BY TOTAL_SALES DESC LIMIT 10;

CREATE OR REPLACE VIEW CUSTOMER_MARKET_COUNT AS
SELECT Market,
COUNT(Customer_Id) AS CUSTOMER_COUNT
FROM  DATACO_RAW
GROUP BY Market;\

CREATE OR REPLACE VIEW  VW_CUSTOMER_MARKET_KPIS_SALES_PER_CUSTOMER AS
SELECT
COUNT(DISTINCT CUSTOMER_ID) AS UNIQUE_CUSTOMERS,
ROUND(SUM(SALES) / NULLIF(COUNT(DISTINCT CUSTOMER_ID), 0),2)AS SALES_PER_CUSTOMER,
ROUND(COUNT(DISTINCT ORDER_ID) / NULLIF(COUNT(DISTINCT CUSTOMER_ID), 0),2) AS  ORDERS_PER_CUSTOMER,
(SELECT MARKET FROM DATACO_RAW GROUP BY MARKET ORDER BY SUM(SALES) DESC LIMIT 1) AS TOP_MARKET
FROM DATACO_RAW;











CREATE OR REPLACE VIEW VW_DELIVERY_KPIS AS
SELECT
ROUND(COUNT(DISTINCT CASE WHEN Delivery_Status = 'Late delivery' THEN Order_Id END)/NULLIF(COUNT(DISTINCT Order_Id),0)*100,2) AS LATE_DELIVERY_RATE,
ROUND(COUNT(DISTINCT CASE WHEN Delivery_Status = 'Shipping on time' THEN Order_Id END)/NULLIF(COUNT(DISTINCT Order_Id),0)*100,2) AS ON_TIME_RATE,
ROUND(AVG(Shipping_Delay),2) AS AVERAGE_SHIPPING_DELAY,
(SELECT COUNT(DISTINCT Order_Id) FROM   DATACO_RAW WHERE Shipping_Delay > 0) AS HIGH_RISK_ORDERS
FROM
DATACO_RAW;

CREATE OR REPLACE VIEW Late_Delivery_Rate_by_Shipping_Mode AS
SELECT
ROUND(COUNT(DISTINCT CASE WHEN Delivery_Status = 'Late delivery' THEN Order_Id END)/NULLIF(COUNT(DISTINCT Order_Id),0)*100,2) AS LATE_DELIVERY_RATE,
Shipping_Mode
FROM DATACO_RAW GROUP BY Shipping_Mode;

CREATE OR REPLACE VIEW AVG_DELAYBYMARKET AS
SELECT
ROUND(AVG(Shipping_Delay),2) AS AVG_SHIPPING_DELAY,
Market
FROM DATACO_RAW
GROUP BY Market;

CREATE OR REPLACE VIEW AVG_SHIPPING_DELAYBYMARKET AS
SELECT
ROUND(COUNT(DISTINCT CASE WHEN Delivery_Status = 'Late delivery' THEN Order_Id END)/NULLIF(COUNT(DISTINCT Order_Id),0)*100,2) AS LATE_DELIVERY_RATE,
Category_Name
FROM DATACO_RAW GROUP BY Category_Name;


CREATE OR REPLACE VIEW VW_ACTUAL_VS_SCHEDULED_SHIPPING AS
SELECT
SHIPPING_MODE,
 ROUND(AVG(DAYS_FOR_SHIPPING_REAL), 2) AS AVG_ACTUAL_SHIPPING_DAYS,
ROUND(AVG(DAYS_FOR_SHIPMENT_SCHEDULED), 2) AS AVG_SCHEDULED_SHIPPING_DAYS
FROM DATACO_RAW
GROUP BY SHIPPING_MODE;

CREATE OR REPLACE VIEW Delivery_Risk_Analaysis AS
SELECT
COUNT(DISTINCT Order_Id) AS ORDER_COUNT,
COUNT( DISTINCT CASE WHEN Shipping_Delay > 0 THEN Order_Id END) AS HIGH_RISK_ORDERS,
COUNT( DISTINCT CASE WHEN Shipping_Delay > 0 THEN Order_Id END)/NULLIF(COUNT(DISTINCT Order_Id),0) AS HIGH_RISK_RATE,
ROUND(AVG(Shipping_Delay),2) AS AVERAGE_SHIPPING_DELAY,
MARKET, SHIPPING_MODE
FROM
DATACO_RAW GROUP BY MARKET, SHIPPING_MODE;


CREATE OR REPLACE VIEW Shipping_Delay_by_Month AS
SELECT
ROUND(AVG(Shipping_Delay),2) AS AVG_SHIPING_DELAY,
Order_Month,
Order_Year
FROM DATACO_RAW GROUP BY Order_Month,Order_Year;

SELECT
ROUND(AVG(Shipping_Delay),2) AS AVG_SHIPING_DELAY,
Order_Month,
Order_Year
FROM DATACO_RAW GROUP BY Order_Month,Order_Year;














