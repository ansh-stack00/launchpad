import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_classif
import json
from pathlib import Path

OUTPUT_DIR=Path("src/data/processed")


def select_features():
    X_train=pd.read_csv("src/data/processed/X_train.csv")
    X_test=pd.read_csv("src/data/processed/X_test.csv")
    y_train=pd.read_csv("src/data/processed/y_train.csv")
    y_test=pd.read_csv("src/data/processed/y_test.csv")

    corr = X_train.corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
    X_train = X_train.drop(columns=to_drop)
    X_test = X_test.drop(columns=to_drop)

#  calculating mi socre
    mi_scores = mutual_info_classif(X_train, y_train)
    mi_scores = pd.Series(mi_scores, index=X_train.columns)
    selected_features = mi_scores[mi_scores > mi_scores.mean()].index.tolist()
    X_train = X_train[selected_features]
    X_test = X_test[selected_features]

    with open("src/features/feature_list.json", "w") as f:
        json.dump(selected_features, f, indent=4)

    X_train.to_csv(OUTPUT_DIR / "X_train.csv", index=False)
    X_test.to_csv(OUTPUT_DIR / "X_test.csv", index=False)
    y_train.to_csv(OUTPUT_DIR / "y_train.csv", index=False)
    y_test.to_csv(OUTPUT_DIR / "y_test.csv", index=False)
    

if __name__ == "__main__":
    select_features()