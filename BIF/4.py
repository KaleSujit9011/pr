
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.read_csv("gene_expression_medium_dataset.csv")
df = df.drop(columns="Sample_ID")

X = df.drop(columns="Class")
y = df["Class"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
prediction = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, prediction))
print("Confusion matrix:\n", confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))
print("Feature importance:\n", pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False))
