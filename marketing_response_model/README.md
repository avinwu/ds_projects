# Marketing Response Modeling


## Overview

### Business Scenario
The company offers their customers personal and auto loans that help them take control of their lives and their finances. **Direct mail** is one important way the marketing team can connect with customers whom may be in need of a loan.

Direct offers provide huge value to customers who need them, and are a fundamental part of company's marketing strategy. In order to improve their targeted efforts, the company must be sure they are focusing on the customers who are likely to respond and be good candidates for their services.

### What to Predict?
Using a large set of anonymized features, the objective is to **predict which customers will respond to a direct mail offer**.

### Evaluation
Evaluation will be based on **area under the ROC curve** between the predicted probability and the observed target.

## Data
Provided a high-dimensional dataset of anonymized customer information. Each row corresponds to one customer. The response variable is binary and labeled "target". You must predict the target variable for every row in the test set.

The features have been anonymized to protect privacy and are comprised of a mix of continuous and categorical features. You will encounter many "placeholder" values in the data, which represent cases such as missing values. We have intentionally preserved their encoding to match with internal systems at Springleaf. The meaning of the features, their values, and their types are provided "as-is" for this competition; handling a huge number of messy features is part of the challenge here.