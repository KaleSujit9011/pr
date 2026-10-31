import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DMV/Retail_Sales_Data.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

regional_sales = df.groupby("State")["Sales"].sum()
regional_sales = regional_sales.sort_values(ascending=False)
print("\nTotal Sales by Region:")
print(regional_sales)

regional_sales.plot(kind="pie",autopct="%.2f%%")
plt.title("Regional Sales Distribution")
plt.show()

print("Top Region:", regional_sales.idxmax())
print("Highest Sales:", regional_sales.max())

category_sales = df.groupby(
    ["State", "Shop_Category"]
)["Sales"].sum().unstack()
print("\nSales by Region and Shop Category:")
print(category_sales)

category_sales.plot(kind="bar", figsize=(10, 5))
plt.title("Category-wise Sales Comparison")
plt.xlabel("State")
plt.ylabel("Total Sales")
plt.legend(title="Shop Category")
plt.tight_layout()
plt.show()
