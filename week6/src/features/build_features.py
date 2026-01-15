import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import json
import pickle

df = pd.read_csv("src/data/processed/final.csv")

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

df["FarePerPerson"] = df["Fare"] / df["FamilySize"]
df["LogFare"] = np.log1p(df["Fare"])

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 60, 100],
    labels=["Child", "Teen", "Adult", "Elder"]
)


df["Title"] = df["Name"].str.extract(r" ([A-Za-z]+)\.", expand=False)
df["Title"] = df["Title"].replace(["Dr", "Rev", "Col", "Major", "Capt", "Jonkheer", "Sir", "Lady", "Countess", "Don"], "Rare")

df["Age*Class"] = df["Age"] * df["Pclass"]
df["Fare*Class"] = df["Fare"] * df["Pclass"]

X = df.drop("Survived", axis=1)
y = df["Survived"]


categorical_cols = ["Sex", "Embarked", "Title", "AgeGroup", "Pclass"]
X = pd.get_dummies(X, columns=categorical_cols, drop_first=False)  


num_cols = ["Age", "Fare", "FamilySize", "FarePerPerson", "LogFare", "Age*Class", "Fare*Class"]
scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])


X.to_csv("src/data/processed/X_features.csv", index=False)
y.to_csv("src/data/processed/y.csv", index=False)


feature_list = X.columns.tolist()
with open("src/data/features/feature_list.json", "w") as f:
    json.dump(feature_list, f)

with open("src/data/processed/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("eature engineering completed")
print(f"Number of features: {len(feature_list)}")
