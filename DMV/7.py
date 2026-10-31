import pandas as pd
import matplotlib.pyplot as plt

salesCSV = pd.read_csv("sales_data.csv")
salesJSON = pd.read_json("sales_data.json")
salesExcel = pd.read_excel("sales_data.xlsx")

for name, data in [("CSV", salesCSV), ("JSON", salesJSON), ("Excel", salesExcel)]:
    print(name, "Data:")
    print(data.head())
    data.info()

print("missing values in CSV:")
print(salesCSV.isnull().sum())

print("\nmissing values in JSON:")
print(salesJSON.isnull().sum())

print("\nmissing values in Excel:")
print(salesExcel.isnull().sum())

def cleaning_data(data):
    data.dropna(inplace=True)
    data["Date"] = pd.to_datetime(data["Date"])
    data.drop_duplicates(inplace=True)
    return data

for data in [salesCSV, salesJSON, salesExcel]:
    cleaning_data(data)

salesCSV["source"] = "CSV"
salesJSON["source"] = "JSON"
salesExcel["source"] = "Excel"

df = pd.concat([salesCSV, salesExcel, salesJSON], ignore_index=True)
print("combined shape:", df.shape)
df = df.drop_duplicates(subset="Order_ID").reset_index(drop=True)
print("unique orders:", len(df))
print(df.head())

df["total_sales"] = df["Quantity"] * df["Price"]
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_name"] = df["Date"].dt.month_name()

print(df.head())

total_sales = df["total_sales"].sum()
average_order_value = df["total_sales"].mean()

print("Total sales:", round(total_sales, 2))
print("Average order value:", round(average_order_value, 2))

product_sales = df.groupby("Product")["total_sales"].sum()
print(product_sales)
product_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["total_sales"].sum()
monthly_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()