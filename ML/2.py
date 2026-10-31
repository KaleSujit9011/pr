import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("uber.csv")

print(df.head())
print("missing values:\n", df.isnull().sum())

df = df.drop(columns=["Unnamed: 0", "key", "pickup_datetime"], errors="ignore")
df = df.dropna()

df = df[
    (df["fare_amount"] > 0) &
    (df["fare_amount"] < 100) &
    (df["pickup_longitude"].between(-75, -72)) &
    (df["dropoff_longitude"].between(-75, -72)) &
    (df["pickup_latitude"].between(39, 42)) &
    (df["dropoff_latitude"].between(39, 42)) &
    (df["passenger_count"].between(1, 6))
]

print("Cleaned dataset:", df.shape)

plt.boxplot(df["fare_amount"])
plt.title("outliers in Uber Fare")
plt.show()

print("Outliers:", df[df["fare_amount"] > 50].shape[0])

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Lasso Regression": Lasso(alpha=0.1, max_iter=10000)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("\n", name)
    print("R2 Score:", round(r2, 4))
    print("RMSE:", round(rmse, 4))