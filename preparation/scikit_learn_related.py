import pandas as pd

from utils import Stage


class CategoricalToNumerical(Stage):
    def run(self, all_data):
        # all classes in sklearn requires numeric data only
        # transform categorical features to numerical
        X = pd.get_dummies(all_data, sparse=True)
        return X.fillna(0)


def get_stages():
    return [CategoricalToNumerical()]
