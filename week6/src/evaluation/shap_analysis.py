import shap
import matplotlib.pyplot as plt

def explain_model_with_shap(model, X_train):
    # Creating a SHAP explainer object
    explainer = shap.TreeExplainer(model)  # Use TreeExplainer for tree-based models (RF, XGBoost)
    
    # Computing SHAP values for training data
    shap_values = explainer.shap_values(X_train)

    # Plotting SHAP summary plot to visualize feature importance
    shap.summary_plot(shap_values, X_train)

    return shap_values

def plot_feature_importance(model, X_train):
    # Feature importance (RandomForest)
    feature_importance = model.feature_importances_
    sorted_idx = feature_importance.argsort()

    # Plotting the feature importance
    plt.figure(figsize=(10, 6))
    plt.barh(X_train.columns[sorted_idx], feature_importance[sorted_idx])
    plt.xlabel('Feature Importance')
    plt.title('Feature Importance from the Model')
    plt.show()
