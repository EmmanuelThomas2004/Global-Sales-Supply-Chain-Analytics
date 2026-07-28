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

