import pandas as pd
from pathlib import Path
from scipy.stats import ks_2samp

TRAIN_PATH = Path("src/data/processed/X_train.csv")
LOG_PATH = Path("src/logs/prediction_logs.csv")

THRESHOLD = 0.05
def check_drift():
    X_train = pd.read_csv(TRAIN_PATH)
    logs = pd.read_csv(LOG_PATH)

    drift_report = {}

    for col in X_train.columns:
        if col not in logs:
            continue

        _, p_value = ks_2samp(X_train[col], logs[col])
        drift_report[col] = {
            "p_value": p_value,
            "drift_detected": p_value < THRESHOLD
        }

    report_df = pd.DataFrame(drift_report).T
    print(report_df.sort_values("p_value").head(10))

    return report_df


if __name__ == "__main__":
    check_drift()
