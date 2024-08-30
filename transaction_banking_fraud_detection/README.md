# Credit Card Fraud Detection

**(Identify fraudulent credit card transactions.)**

## 0. Overview
It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.

The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

## 1. Data Collection
- Import and load the dataset
- Use API if needed to collect data

## 2. Data Exploration & Visualization
- Categorical and Contunuous variables : Identify, Descriptive Statistics
- Check missing values
- Draw visualizations
- Outlier detection
- Relationship between Dependent and Independent variables.
- Relationship among Dependent variables (Correlation matrix).

## 3. Pre-processing
- Detect and remove null records.
- Detect and remove empty strings.
- Categorical to Numerical Variable conversion (Integer Encoding, One-hot encoding)
- Outlier Removal
- Stratified sampling
- Split data into train/test
- Stopword removal, Stemming, Lemmatization (NLP)

## 4. Feature Engineering
- Feature Engineering (Create new features from existing variables)
- Feature Selection - Define Dependent Variable (y) and Independent Variable (x)
- Vectorization (TF-IDF)

## 5. Model Building
- Import - Import the Model.
- Instantiate - Create instance of the Model.
- Fit - Fit the model with training data.
- Predict - Predict Model with test data.

## 6. Model Evaluation
- Confusion Matrix
- Classification Report
- Accuracy Score
- AUC-ROC Curve

## 7. Model Prediction with new Data
- Feed new data to the model and check prediction.

## 8. Conclusion and Recommendations
- (Describe the conclusion and recommendation based on model analysis.)