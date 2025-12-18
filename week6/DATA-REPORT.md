# Data Report: Titanic Dataset

## 1. **Project Overview**
This project is focused on processing and analyzing the Titanic dataset. The primary tasks are:
- **Data Cleaning**: Handle missing values, duplicates, and outliers.
- **Exploratory Data Analysis (EDA)**: Visualize and understand the dataset's key features and relationships.
  
### Dataset:
- **Source**: Titanic dataset (available from Kaggle)
- **Columns**:
  - PassengerId, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked, Survived

## 2. **Data Pipeline**
The data pipeline was built in the `data_pipeline.py` script. The steps performed are:

### 2.1 **Data Loading**:
- The dataset was loaded from the raw `train.csv` file located in the `data/raw/` folder.

### 2.2 **Data Cleaning**:
1. **Missing Values**:
   - For **numerical columns**, missing values were replaced with the **mean** of the respective columns.
   - For **categorical columns** (e.g., `Sex`, `Embarked`), missing values were replaced with the **mode** (most frequent value).
   
2. **Duplicates**:
   - Duplicate rows were removed from the dataset to ensure data integrity.

3. **Outliers**:
   - Outliers were detected and removed using the **Z-score method**. Any data point with a Z-score greater than 3 was considered an outlier and removed.

### 2.3 **Saving Cleaned Data**:
- The cleaned dataset was saved to the `data/processed/final.csv` file for further analysis.

## 3. **Exploratory Data Analysis (EDA)**

The EDA was performed in the `EDA.ipynb` notebook. The following analyses and visualizations were created:

### 3.1 **Correlation Matrix**:
A correlation matrix was generated for the numerical columns to identify relationships between features. Strong correlations can help identify which features are most relevant for modeling.

<!-- ![Correlation Matrix](./images/correlation_matrix.png) -->

### 3.2 **Feature Distributions**:
Histograms were generated for each feature to visualize the distribution of values across numerical features.

<!-- ![Feature Distributions](./images/feature_distributions.png) -->

### 3.3 **Target Distribution**:
A **count plot** of the target variable (`Survived`) was created to show the distribution of passengers who survived versus those who did not.

<!-- ![Target Distribution](./images/target_distribution.png) -->

### 3.4 **Missing Values Heatmap**:
A heatmap of missing values was generated to visualize which columns contain missing data.

<!-- ![Missing Values Heatmap](./images/missing_values_heatmap.png) -->

## 4. **Insights from EDA**:

### 4.1 **Correlation Matrix**:
- `Fare` and `Age` are strongly correlated with survival (`Survived`), suggesting that they might be significant features for predicting survival.
- `SibSp` and `Parch` are less correlated with survival but might indicate the importance of family presence.

### 4.2 **Feature Distributions**:
- **Age**: The distribution of ages is skewed towards younger passengers.
- **Fare**: There are some high-value outliers for fare prices.
- **SibSp & Parch**: Most passengers have either no siblings/spouse or parents/children aboard.

### 4.3 **Target Distribution**:
- A relatively balanced distribution between survived (38%) and not survived (62%) passengers.

### 4.4 **Missing Values**:
- **Age** has a significant number of missing values, which were filled with the mean age.
- **Cabin** also has many missing values, which could be ignored for now as it is not critical to the analysis.




### Day2. FEATURE ENGINEERING AND FEATURE SELECTION 

## Overview
This document describes the feature engineering and feature selection process.

## Feature Engineering Steps
1. Loaded cleaned dataset from `data/processed/final.csv`
2. Created new numerical features:
   - Log transformation
   - Square root transformation
   - Squared features
3. Encoded categorical features using One-Hot Encoding
4. Scaled numerical features using StandardScaler
5. Split data into train and test sets

## Feature Selection
- Method: Mutual Information
- Selected top 20 most important features
- Feature importance plot generated

## Output Files
- X_train.npy
- X_test.npy
- y_train.npy
- y_test.npy
- feature_list.json
- selected_features.json

-------




# Day 3 — Model Building & Training Pipeline (Titanic Dataset)

## Objective
The goal of Day 3 is to build a robust and reusable machine learning training pipeline
that trains multiple models, evaluates them using cross-validation, compares performance,
and automatically selects and saves the best model.

---

## Dataset
**Name:** Titanic Survival Dataset  
**Target Variable:** `Survived`  
- `0` → Passenger did not survive  
- `1` → Passenger survived  

The dataset used for training was preprocessed and feature-engineered during Day 1 and Day 2.

---

## Models Trained
The following models were trained and evaluated:

1. **Logistic Regression**
   - Linear baseline model
   - Used L2 regularization
   - Class imbalance handled using `class_weight="balanced"`

2. **Random Forest Classifier**
   - Ensemble-based tree model
   - Captures non-linear feature interactions
   - Robust to outliers and feature scaling

3. **Gradient Boosting / XGBoost**
   - Boosting-based ensemble model
   - Improves performance by correcting previous errors
   - Provides strong results on tabular data

4. **Neural Network (MLPClassifier)**
   - Multi-layer perceptron
   - Captures complex patterns
   - Requires scaled input features

---

## Training Strategy

### Cross-Validation
- **Method:** Stratified K-Fold Cross-Validation
- **Number of folds:** 5
- Ensures class balance in each fold
- Helps prevent overfitting and underfitting

### Evaluation Metrics
Each model was evaluated using the following metrics:

- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **ROC-AUC**

The **F1 Score** was used as the primary metric for model selection due to class imbalance.

---

## Model Comparison Summary

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|------|----------|-----------|--------|----------|---------|
| Logistic Regression | Recorded | Recorded | Recorded | Recorded | Recorded |
| Random Forest | Recorded | Recorded | Recorded | Recorded | Recorded |
| Gradient Boosting / XGBoost | Recorded | Recorded | Recorded | Recorded | Recorded |
| Neural Network | Recorded | Recorded | Recorded | Recorded | Recorded |

*(Exact values are stored in `src/evaluation/metrics.json`)*

---

## Best Model Selection

### Best Model
**Random Forest Classifier** **

### Selection Criteria
- Highest **F1 Score** on test data
- Balanced precision and recall
- Stable cross-validation performance

---

## Model Artifacts

The following artifacts were generated automatically:



