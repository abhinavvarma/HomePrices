import numpy
from scikits.statsmodels.tools import categorical
import graphlab

def get_train_data():
    return graphlab.SFrame('/home/abhinav/Desktop/WORKSPACE/HomePrices/dataset/train.csv')

def get_test_data():
    return graphlab.SFrame('/home/abhinav/Desktop/WORKSPACE/HomePrices/dataset/test.csv')


def get_correlation():
    pd_house_train_data = get_train_data().to_dataframe()
    corr = pd_house_train_data.select_dtypes(include=['float64', 'int64']).corr()
    cor_dict = corr['SalePrice'].to_dict()
    del cor_dict['SalePrice']
    return cor_dict



def get_correlation2():
    target_feature = "SalePrice"
    target_series = df[target_feature]

    for feature in df:
        print feature , "vs", target_feature
        numerical_series = categorical(df[feature], drop=True).argmax(1)
        print numpy.corrcoef(df[feature], target_series)[0, 1]

    print df.describe()


def get_variables():
    import csv
    variables = {}
    data = get_train_data()
    test_data = get_test_data()
    correlation = get_correlation()

    Categorical_columns = list(data.to_dataframe().select_dtypes(include=['object']).columns.values)

    with open('/home/abhinav/Desktop/WORKSPACE/HomePrices/dataset/variables.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=':')
    
        for row in spamreader:
            variable_name = row[0]
            corr = "-"
            if variable_name in correlation:
                corr = "%.4f" % correlation.get(variable_name, 0)
            variables[row[0]] = {
                "name": variable_name,
                "description": row[1],
                "type": "Categorical" if (variable_name in Categorical_columns) else "Numerical",
                "correlation": corr,
                "missingTrain": "%.2f" % ((float(data[variable_name].num_missing())/ len(data[variable_name])) * 100.0),
                "missingTest": "%.2f" % ((float(test_data[variable_name].num_missing()) / len(test_data[variable_name])) * 100.0 if variable_name != "SalePrice" else 0)
            }

    return variables

get_correlation()