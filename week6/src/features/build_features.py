import pandas as pd 
import numpy as np 
import json 
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
FEATURES_DIR = PROJECT_ROOT / "src" / "features"
PROCESSED_DIR = PROJECT_ROOT / "src" / "data" / "processed"

# loading cleaned dataset 

DATA_PATH=os.path.join(os.getcwd(),PROCESSED_DIR/'final.csv')
TARGET="Survived"

df=pd.read_csv(DATA_PATH)
print("Data loaded ",df.shape)


# doing feature engineering

# 1. family size 
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# 2.Is passenger alone?
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)


# 3.Fare per person
df["FarePerPerson"] = df["Fare"] / df["FamilySize"]

# 4.Log Fare 
df["LogFare"] = np.log1p(df["Fare"])

# 5.Age groups
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 60, 100],
    labels=["Child", "Teen", "Adult", "Elder"]
)


# Extract title from Name
df["Title"] = df["Name"].str.extract(r" ([A-Za-z]+)\.", expand=False)

# Group rare titles
df["Title"] = df["Title"].replace(
    ["Lady", "Countess", "Capt", "Col", "Don", "Dr",
     "Major", "Rev", "Sir", "Jonkheer", "Dona"],
    "Rare"
)
df["Title"] = df["Title"].replace({"Mlle": "Miss", "Ms": "Miss", "Mme": "Mrs"})

print("Feature engineering completed")


X = df.drop(columns=[TARGET])
y = df[TARGET]

numerical_features = [
    "Age", "Fare", "SibSp", "Parch",
    "FamilySize", "FarePerPerson", "LogFare"
]

categorical_features = [
    "Sex", "Embarked", "Pclass", "Title", "AgeGroup"
]


numeric_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline(steps=[
    ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_pipeline, numerical_features),
        ("cat", categorical_pipeline, categorical_features)
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)


feature_names = (
    numerical_features +
    list(
        preprocessor
        .named_transformers_["cat"]
        .named_steps["onehot"]
        .get_feature_names_out(categorical_features)
    )
)

with open(FEATURES_DIR / "feature_list.json", "w") as f:
    json.dump(feature_names, f, indent=4)

np.save(PROCESSED_DIR/"X_train.npy", X_train_processed)
np.save(PROCESSED_DIR/"X_test.npy", X_test_processed)
np.save(PROCESSED_DIR/"y_train.npy", y_train)
np.save(PROCESSED_DIR/"y_test.npy", y_test)

print("Processed Titanic features saved successfully")

