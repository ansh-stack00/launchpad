import pandas as pd
import numpy as np
import os

SRC_FILE_PATH = os.path.join(os.getcwd(), '../data/raw/train.csv')
DEST_FILE_PATH = os.path.join(os.getcwd(), '../data/processed/final.csv')

# loading the dataset 

def load_data():
    data = pd.read_csv(SRC_FILE_PATH)
    return data 

# cleaning the data 

def clean_data(data):
    # Handling missing values for numeric columns
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

    # Handling missing values for categorical columns (fill with mode)
    categorical_cols = data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        data[col] = data[col].fillna(data[col].mode()[0])

    # Handling duplicates
    data = data.drop_duplicates()

    # Handling outliers using Z-score (numeric columns only)
    from scipy import stats
    z_scores = np.abs(stats.zscore(data.select_dtypes(include=[np.number])))
    data = data[(z_scores < 3).all(axis=1)]

    return data

# saving the cleaned data 

def save_cleaned_data(data):
    data.to_csv(DEST_FILE_PATH , index=False)


def main():
    data = load_data()
    cleaned_data = clean_data(data)
    save_cleaned_data(cleaned_data)
    print("Data processing complete and saved to /data/processed/final.csv")


if __name__ == "__main__":
    main()