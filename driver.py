import numpy as np
import pandas as pd
from sklearn import linear_model

import preparation
import preprocessing

def split_xy(all_data):
    x = all_data.loc[:, 'MSSubClass':'SaleCondition']
    y = all_data.SalePrice
    return x, y

def partition(x, y):
    partition = x.shape[0] *2/3
    x_train = x[:partition]
    y_train = y[:partition]
    x_test = x[partition:]
    y_test = y[partition:]
    return x_train, y_train, x_test, y_test

def train(X_train, y_train):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X_train, y_train)
    return regr

def evaluate(model, x_test, y_test):
    # The mean squared error
    print("Mean squared error: %.2f"
          % np.mean((model.predict(x_test) - y_test) ** 2)
          )
    # Explained variance score: 1 is perfect prediction
    print('R Square: %.2f' % model.score(x_test, y_test))

def run_preprocessing_stages(preprocessing_stages):
    training_data = pd.read_csv("./dataset/train.csv")
    x, y = split_xy(training_data)
    # x_processed = preprocessing.run(x)
    x_processed = preprocessing.run_stages(x, preprocessing_stages)
    x_processed = preparation.run(x_processed)
    x_train, y_train, x_test, y_test = partition(x_processed, y)
    model = train(x_train, y_train)
    evaluate(model, x_test, y_test)


def calculate_preprocessing_effect():
    run_preprocessing_stages([])
    for stage in preprocessing.get_stages():
        print "---------------------------------------"
        run_preprocessing_stages([stage])

def run_everything():
    run_preprocessing_stages(preprocessing.get_stages())

if __name__ == '__main__':
    calculate_preprocessing_effect()