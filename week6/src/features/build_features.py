import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_PATH = Path("src/data/processed/final.csv")
OUTPUT_DIR=Path("src/data/processed")



def extract_title(name):
    return name.split(",")[1].split(".")[0].strip()

def age_group(age):
    if age <= 12:
        return "Child"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior"

def build_feature():
    df = pd.read_csv(DATA_PATH)

    y = df["Survived"]
    df = df.drop(columns=["Survived"])

    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = (df["FamilySize"] == 1).astype(int)
    df["FarePerPerson"] = df["Fare"] / df["FamilySize"]
    df["LogFare"] = np.log1p(df["Fare"])
    df["AgeSquared"] = df["Age"] ** 2
    df["HighFare"] = (df["Fare"] > df["Fare"].median()).astype(int)

    # Age groups
    df["AgeGroup"] = df["Age"].apply(age_group)

# extracting title 
    df["Title"] = df["Name"].apply(extract_title)

    df = df.drop(columns=["Name", "Ticket"])

    df = pd.get_dummies(df, columns=["Embarked", "AgeGroup", "Title"], drop_first=True)
    
    scaler = StandardScaler()
    numerical_cols = df.select_dtypes(include=np.number).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    X_train, X_test, y_train, y_test = train_test_split(
        df, y, test_size=0.2, random_state=42, stratify=y
    )

    
    X_train.to_csv(OUTPUT_DIR / "X_train.csv", index=False)
    X_test.to_csv(OUTPUT_DIR / "X_test.csv", index=False)
    y_train.to_csv(OUTPUT_DIR / "y_train.csv", index=False)
    y_test.to_csv(OUTPUT_DIR / "y_test.csv", index=False)

    print("Saved: X_train.csv, X_test.csv, y_train.csv, y_test.csv")


if __name__ == "__main__":
    build_feature()
