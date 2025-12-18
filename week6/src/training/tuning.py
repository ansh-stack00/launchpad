from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import optuna

def grid_search_tuning(X_train, y_train, X_test, y_test):
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Initializing  model
    model = RandomForestClassifier(random_state=42)

    # Initializing GridSearchCV
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy', verbose=1, n_jobs=-1)

    # Fitting the grid search
    grid_search.fit(X_train, y_train)

    # Get best model and parameters
    best_model = grid_search.best_estimator_
    print("Best Parameters: ", grid_search.best_params_)

    # Evaluating the best model
    y_pred = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of the best model: {accuracy:.4f}")

    return best_model, grid_search.best_params_

def optuna_tuning(X_train, y_train, X_test, y_test):
    def objective(trial):
        n_estimators = trial.suggest_int('n_estimators', 50, 200)
        max_depth = trial.suggest_int('max_depth', 10, 30)
        min_samples_split = trial.suggest_int('min_samples_split', 2, 10)
        min_samples_leaf = trial.suggest_int('min_samples_leaf', 1, 4)

        model = RandomForestClassifier(n_estimators=n_estimators,
                                       max_depth=max_depth,
                                       min_samples_split=min_samples_split,
                                       min_samples_leaf=min_samples_leaf,
                                       random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy

    # Creating an Optuna study and optimize it
    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=100)

    best_trial = study.best_trial
    print("Best Trial: ", best_trial.params)

    return best_trial
