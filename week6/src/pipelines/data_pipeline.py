import pandas as pd
import numpy as np
import os

SRC_FILE_PATH = os.path.join(os.getcwd(), 'src/data/raw/train.csv')
DEST_FILE_PATH = os.path.join(os.getcwd(), 'src/data/processed/final.csv')

# loading the dataset 

def load_data():
    data = pd.read_csv(SRC_FILE_PATH)
    return data 

# cleaning the data 

def clean_data(data):
    # Handling missing values for numeric columns
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

    # Handling missing values for categorical columns 
    categorical_cols = data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        
        data[col] = data[col].fillna(data[col].mode()[0])
        # print(data[col])

    # Handling duplicates
    data = data.drop_duplicates()

    
    def remove_outliers_iqr(data, cols):
        for col in cols:
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
        return data
    
    data = remove_outliers_iqr(data, ['Age', 'Fare'])
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