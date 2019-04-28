# Supervised Learning with scikit-learn
[Course link](https://www.datacamp.com/courses/supervised-learning-with-scikit-learn)

[Introduction to Machine Learning with Python](https://github.com/amueller/introduction_to_ml_with_python)
#### 1. Classification
* Supervised Learning
* Exploratory Data Analysis (EDA)
    * Numerical EDA and Visual EDA
* k-Nearest Neighbors:
    * KNeighborsClassifier
    * fit and predict
* Measuring model performance
    * sklearn.model_selection.train_test_split
    * Overfitting and underfitting
#### 2. Regression
* Introduction to Regression
    * Creating feature and target arrays:
    ```
        X = df.drop('target', axis=1).values
        X = X.reshape(-1, 1)
        y = df('target').values
        y = y.reshape(-1, 1)
    ```
    * sklearn.linear_model.LinearRegression()
    * Fitting a regression model
* The basics of linear regression
    * Ordinary least squares (OLS)
* Cross-validation (evaluating model)
    * sklearn.model_selection.cross_val_score
* Regularized regression
    * Lasso: sklearn.linear_model.Lasso
    * Ridge: sklearn.linear_model.Ridge
#### 3. Fine-tuning your model
* How good is your model?
    * Confusion matrix: sklearn.metrics.confusion_matrix
    * Classification report: sklear.metric.classification_report
* Logistic regression and the ROC curve
    * Logistic Regression: sklearn.linear_model.LogisticRegression
    * Plotting the ROC curve: sklearn.metrics.roc_curve
    * Precissio-recall curve: sklearn.metrics.precission_recall_curve
* Area under the ROC curve (AUC): Larger area under ROC curve = better model
    * AUC: sklearn.metrics.roc_auc_curve
* Hyperparameter tuning
    * Choosing the correct hyperparameter
    * GridSearchCV: sklearn.model_selection.GridSearchCV
    * Decision Tree: sklearn.tree.DecisionTreeClassifier
    * RandomizedSearchCV: sklearn.model_selection.RandomizedSearchCV
* Hold-out set for final evaluation
    * Hold-out set reasoning
#### 4. Preprocessing and pipelines
* Preprocessing data
    * Dealing with categorical features
    ```
    scikit-learn: OneHotEncoder()
    pandas: get_dummies()
    ```
* Handling missing data
    * Dropping missing data
    * Imputting missing data in a ML Pipeline
        * sklearn.preprocessing.Imputer
        * sklearn.svm.SVC
        * sklearn.pipeline.Pipeline
* Centering and scaling
    * Scaling: sklearn.preprocessing.scale
