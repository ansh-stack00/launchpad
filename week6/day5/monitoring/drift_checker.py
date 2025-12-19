import numpy as np
import pandas as pd
import joblib

class DriftChecker:
    def __init__(self, model_path, baseline_data_path):
        # Loading the trained model and baseline data
        self.model = joblib.load(model_path)
        self.baseline_data = pd.read_csv(baseline_data_path)
        self.baseline_mean = self.baseline_data.mean()
        self.baseline_std = self.baseline_data.std()

    def check_data_drift(self, new_data):
        """
        Compares the statistical properties of the new data with baseline data.
        """
        # Calculate mean and std of new data
        new_data_mean = new_data.mean()
        new_data_std = new_data.std()

        # Calculate differences
        mean_diff = np.abs(self.baseline_mean - new_data_mean)
        std_diff = np.abs(self.baseline_std - new_data_std)

        drift_alert = False
        drift_report = {}

        # If mean or std deviation differences are above a threshold, flag as drift
        if any(mean_diff > 0.1) or any(std_diff > 0.1):  # Threshold is an example, can be tuned
            drift_alert = True
            drift_report = {
                "mean_diff": mean_diff,
                "std_diff": std_diff
            }

        return drift_alert, drift_report

    def log_drift(self, drift_alert, drift_report):
        """
        Logs data drift alerts and reports.
        """
        if drift_alert:
            print("Data drift detected!")
            print(drift_report)
        else:
            print("No significant data drift detected.")
        
        # Optionally, save the drift report to a file or log it as needed.
        # Here, we can log to a file or database, depending on the implementation.
        with open("drift_log.txt", "a") as log_file:
            log_file.write(str(drift_report) + "\n")
