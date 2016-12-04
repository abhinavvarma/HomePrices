import numpy as np
import pandas as pd
from math import sqrt
from sklearn import linear_model

import preparation
import preprocessing
from preprocessing import outlier_analysis


def split_xy(all_data):
    x = all_data.loc[:, 'MSSubClass':'SaleCondition']
    y = all_data.SalePrice
    return x, y


def partition(x, y):
    partition = x.shape[0] * 2 / 3
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
    # print (model.predict(x_test) - y_test)
    # The mean squared error
    rmse = sqrt(np.mean((model.predict(x_test) - y_test) ** 2))
    print("Mean squared error: %f"% rmse)
    # Explained variance score: 1 is perfect prediction
    r_square = model.score(x_test, y_test)
    print('R Square: %f' % r_square)
    return r_square

def normalize_target(series):
    # log transform the target:
    return np.log1p(series)

def run_preprocessing_stages(preprocessing_stages):
    training_data = pd.read_csv("./dataset/train.csv")
    training_data = outlier_analysis.DropRows().run(training_data)
    x, y = split_xy(training_data)
    # x_processed = preprocessing.run(x)
    x_processed = preprocessing.run_stages(x, preprocessing_stages)
    x_processed = preparation.run(x_processed)
    x_train, y_train, x_test, y_test = partition(x_processed, y)
    model = train(x_train, normalize_target(y_train))
    return evaluate(model, x_test, normalize_target(y_test))

def cmp(a,b):
    if a[0] == b[0]:
        return 0
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1

def calculate_preprocessing_impact():
    impact = []
    impact.append((run_preprocessing_stages([]), None))
    for stage in preprocessing.get_stages():
        print "---------------------------------------"
        impact.append((run_preprocessing_stages([stage]), stage))
    impact.pop(0)
    impact.sort(key=lambda tup: -tup[0])
    # print [(t[0], t[1].cols) for t in impact]
    print impact


def run_everything():
    run_preprocessing_stages(preprocessing.get_stages())


if __name__ == '__main__':
    run_everything()
    # calculate_preprocessing_impact()
