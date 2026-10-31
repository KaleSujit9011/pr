
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("telecom_customer_churn.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().replace("", np.nan)

df["gender"] = df["gender"].str.lower()
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

df["AvgMonthlyCharge"] = (
    df["TotalCharges"] / df["tenure"].replace(0, np.nan)
).fillna(df["MonthlyCharges"])

for col in ["tenure", "MonthlyCharges", "TotalCharges"]:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    df[col] = df[col].clip(q1 - 1.5 * iqr, q3 + 1.5 * iqr)

X = df.drop(columns=["customerID", "Churn"])
y = df["Churn"].map({"No": 0, "Yes": 1})

X = pd.get_dummies(X, drop_first=True, dtype=int)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

cols = ["tenure", "MonthlyCharges", "TotalCharges", "AvgMonthlyCharge"]
scaler = StandardScaler()
X_train[cols] = scaler.fit_transform(X_train[cols])
X_test[cols] = scaler.transform(X_test[cols])

df.to_csv("Telecom_Customer_Churn_Cleaned.csv", index=False)
print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)
print("Cleaned dataset saved successfully!")