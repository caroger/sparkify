# Sparkify - Customer Churn Prediction

## Overview

This is the capstone project for the [Udacity Data Scientist Nanodegree Program](https://www.udacity.com/course/data-scientist-nanodegree--nd025).

The goal of this project is to train a classification model on large amount of data to predict customer churn using Spark. Although the analysis presented here was done on a subset (242MB) of the full data set (12GB) on a local computer, the Spark ML framework used here allows for the analysis to be scaled to much bigger datasets if the code was deployed on a cluster such as AWS and IBM Cloud.

## Installation

Create a python virtual environment with venv or conda, install jupyter notebook.

```bash
# clone repo
git clone git@github.com:caroger/sparkify.git
cd sparkify

# install required packages
pip install -r requirements.txt

# download training data
wget https://video.udacity-data.com/topher/2018/December/5c1d6681_medium-sparkify-event-data/medium-sparkify-event-data.json
```

Run all cells in the `sparkify_local.ipynb` notebook to reproduce the analysis result.

## Analysis and Results

1. Performed EDA and feature engineering on 242MB of data (543,705 rows  x 18 cols )
2. Split data into training (75%) and testing (25%) sets
3. Applied logistic regression, random forest, decision tree, and gradient-boosted tree models on the training data and evaluate the model performance on testing set measured in F1-score
4. Performed hyper-parameter tuning on the top two best performing models - random forest and gradient-boosted tree 
5. The resulting best performing model is random forest classifier with  `numTrees`= 40 and  `maxDepth`=5 as hyper parameters and validation accuracy score below

```python
accuracy: 0.881
precision: 0.8962
recall: 0.881
f1: 0.858
AUC: 0.8276
```

3. Feature Importance

![](https://github.com/caroger/sparkify/blob/master/plots/feature%20importances.png)

4. More detailed write-ups on the analysis can be found on this [medium post](https://medium.com/@handeasy/customer-churn-prediction-with-spark-ml-in-python-c63302aae95)

