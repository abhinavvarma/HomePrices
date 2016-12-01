import numpy as np
from utils import Stage
from scipy.stats import skew

class ReplaceMonth(Stage):
    def run(self, all_data):
        return all_data.replace(
            {
                'MoSold': {
                    1: 'Yan',
                    2: 'Feb',
                    3: 'Mar',
                    4: 'Apr',
                    5: 'May',
                    6: 'Jun',
                    7: 'Jul',
                    8: 'Avg',
                    9: 'Sep',
                    10: 'Oct',
                    11: 'Nov',
                    12: 'Dec'
                }
            }
        )


class ReplaceOrderedStrings(Stage):
    def run(self, all_data):
        return all_data.replace({'Utilities': {'AllPub': 1, 'NoSeWa': 0, 'NoSewr': 0, 'ELO': 0},
                                 'Street': {'Pave': 1, 'Grvl': 0},
                                 'FireplaceQu': {'Ex': 5,
                                                 'Gd': 4,
                                                 'TA': 3,
                                                 'Fa': 2,
                                                 'Po': 1,
                                                 'NoFireplace': 0
                                                 },
                                 'Fence': {'GdPrv': 2,
                                           'GdWo': 2,
                                           'MnPrv': 1,
                                           'MnWw': 1,
                                           'NoFence': 0},
                                 'ExterQual': {'Ex': 5,
                                               'Gd': 4,
                                               'TA': 3,
                                               'Fa': 2,
                                               'Po': 1
                                               },
                                 'ExterCond': {'Ex': 5,
                                               'Gd': 4,
                                               'TA': 3,
                                               'Fa': 2,
                                               'Po': 1
                                               },
                                 'BsmtQual': {'Ex': 5,
                                              'Gd': 4,
                                              'TA': 3,
                                              'Fa': 2,
                                              'Po': 1,
                                              'NoBsmt': 0},
                                 'BsmtExposure': {'Gd': 3,
                                                  'Av': 2,
                                                  'Mn': 1,
                                                  'No': 0,
                                                  'NoBsmt': 0},
                                 'BsmtCond': {'Ex': 5,
                                              'Gd': 4,
                                              'TA': 3,
                                              'Fa': 2,
                                              'Po': 1,
                                              'NoBsmt': 0},
                                 'GarageQual': {'Ex': 5,
                                                'Gd': 4,
                                                'TA': 3,
                                                'Fa': 2,
                                                'Po': 1,
                                                'NoGarage': 0},
                                 'GarageCond': {'Ex': 5,
                                                'Gd': 4,
                                                'TA': 3,
                                                'Fa': 2,
                                                'Po': 1,
                                                'NoGarage': 0},
                                 'KitchenQual': {'Ex': 5,
                                                 'Gd': 4,
                                                 'TA': 3,
                                                 'Fa': 2,
                                                 'Po': 1},
                                 'Functional': {'Typ': 0,
                                                'Min1': 1,
                                                'Min2': 1,
                                                'Mod': 2,
                                                'Maj1': 3,
                                                'Maj2': 4,
                                                'Sev': 5,
                                                'Sal': 6}
                                 })


class LogTransformNumericalFeature(Stage):
    def run(self, all_data):
        # log transform the target:
        # train["SalePrice"] = np.log1p(train["SalePrice"])

        # log transform skewed numeric features:
        numeric_feats = all_data.dtypes[all_data.dtypes != "object"].index

        skewed_feats = all_data[numeric_feats].apply(lambda x: skew(x.dropna()))  # compute skewness
        skewed_feats = skewed_feats[skewed_feats > 0.75]
        skewed_feats = skewed_feats.index

        all_data[skewed_feats] = np.log1p(all_data[skewed_feats])
        return all_data


def get_stages():
    return [ReplaceMonth, ReplaceOrderedStrings, LogTransformNumericalFeature]