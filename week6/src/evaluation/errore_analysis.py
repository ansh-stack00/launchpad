import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap='Blues', xticklabels=["Not Survived", "Survived"], yticklabels=["Not Survived", "Survived"])
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

def analyze_misclassified(X_test, y_test, y_pred):
   
    misclassified = X_test.copy()
    misclassified['True Label'] = y_test
    misclassified['Predicted Label'] = y_pred
    misclassified['Error'] = misclassified['True Label'] != misclassified['Predicted Label']

 
    misclassified = misclassified[misclassified['Error'] == True]

    print("Misclassified Instances:\n", misclassified)
