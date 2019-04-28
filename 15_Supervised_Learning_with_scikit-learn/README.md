# Supervised Learning with scikit-learn
[Course link](https://www.datacamp.com/courses/supervised-learning-with-scikit-learn)

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
