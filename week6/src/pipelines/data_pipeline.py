import pandas as pd
import numpy as np
import os

SRC_FILE_PATH = os.path.join(os.getcwd(), 'src/data/raw/train.csv')
DEST_FILE_PATH = os.path.join(os.getcwd(), 'src/data/processed/final.csv')


def load_Data():
    df=pd.read_csv(SRC_FILE_PATH)
    print(f"data loaded succesfully : {df.shape}")
    # print(df.head())

    return df

def handling_duplicated_values(df):

    # checking duplicated values 
    # print(df.duplicated())
    duplicate_values = df.duplicated().sum()

    if duplicate_values > 0:
        print(df[df.duplicated()])
        df = df.drop_duplicates(inplace=True)
        print(f"removed dupicate valeus")
    else :
        print("no duplicate values found ")
    

    return df

def handling_missing_values(df):
    # show_missed_values = df.isnull().sum()
    # print(show_missed_values)

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # 687 missing values 
    df = df.drop(columns=["Cabin"])
    print(f"after handling missing values  {df.shape}")

    return df


def handle_outliers(df):
    numerical_cols = ["Age", "Fare"]
    for col in numerical_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower) & (df[col] <= upper)]

    return df


def save_processed_data(df):
    df.to_csv(DEST_FILE_PATH, index=False)
    print(f"Processed data saved at {DEST_FILE_PATH}")

    


def run_pipeline():
    df = load_Data()
    df = handling_duplicated_values(df)
    df = handling_missing_values(df)
    df = handle_outliers(df)
    save_processed_data(df)


if __name__ == "__main__":
    run_pipeline()
    