import pandas as pd
df = pd.read_csv("realestate_prices.csv")
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-zA-Z0-9_]", "", regex=True))
print(df.head())

df = df.drop_duplicates()
for col in df.select_dtypes("object"):
    df[col] = df[col].str.strip()
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna()
print("Missing Values:", df.isnull().sum().sum())

large_houses = df[df["sqft_living"] >= 3000]
print("Large Houses:")
print(large_houses.head())

summary = df.groupby("condition")["price"].agg(
    ["count", "mean", "median"])
print(summary)

for col in ["price", "sqft_living"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    print(col, "Outliers:",
          ((df[col] < lower) | (df[col] > upper)).sum())
    df[col] = df[col].clip(lower, upper)

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df = df.drop(columns=["id", "date"])
df["zipcode"] = df["zipcode"].astype(str)
df = pd.get_dummies(df, drop_first=True, dtype=int)
print(df.head())

df.to_csv("cleaned_realestate_prices.csv", index=False)
print("Dataset saved successfully!")
print("Final Shape:", df.shape)