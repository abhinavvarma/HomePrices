import pandas as pd
from sklearn.preprocessing.label import LabelEncoder

from utils import Stage


class CategoricalToNumerical(Stage):
    def run(self, all_data):
        # all classes in sklearn requires numeric data only
        # transform categorical features to numerical
        all_data = pd.get_dummies(all_data, sparse=True)
        return all_data


class FillNANumerical(Stage):
    def run(self, all_data):
        numeric_feats = all_data.dtypes[all_data.dtypes != "object"].index
        for feature in numeric_feats:
            all_data[feature] = all_data[feature].fillna(all_data[feature].mean())
        return all_data


class FillNACategorical(Stage):
    def run(self, all_data):
        # categorical_feats = all_data.dtypes[all_data.dtypes == "object"].index
        # a = LabelEncoder()
        # for categorical_col in categorical_feats:
        #     all_data[categorical_col] = a.fit_transform(all_data[categorical_col])
        all_data = all_data.fillna(all_data.mode())
        return all_data


def get_stages():
    return [FillNANumerical(), FillNACategorical(), CategoricalToNumerical()]
