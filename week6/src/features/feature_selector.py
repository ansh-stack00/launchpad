import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_classif
import json
from src.features.build_features import build_feature

def select_features():
    X_train, X_test, y_train, y_test = build_feature()

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

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    select_features()