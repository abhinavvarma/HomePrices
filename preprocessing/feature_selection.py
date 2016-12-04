from utils import Stage


class DropColumn(Stage):
    def __init__(self, cols):
        self.cols = cols

    def __str__(self):
        return ".".join([self.__module__, self.__class__.__name__, "_".join(self.cols)])

    def run(self, all_data):
        for col in self.cols:
            all_data = all_data.drop(col, 1)
        return all_data


def get_combined():
    l = [(0.82369823666195519, 'GrLivArea'), (0.82369823666195685, 'BsmtUnfSF'), (0.82369823666196829, 'BsmtFinSF2'),
         (0.82370138871406418, 'MasVnrArea'), (0.82372079177733304, 'MiscVal'), (0.82372575464538744, 'BedroomAbvGr'),
         (0.82373139737294521, 'OpenPorchSF'), (0.82376191065774784, 'MSSubClass'),
         (0.82383761947767531, 'BsmtFinType2'), (0.82384758543502246, 'GarageType'),
         (0.82390961410196195, 'HouseStyle'), (0.82393231571339387, 'MoSold'), (0.82394616561091905, 'ExterCond'),
         (0.82407952012907271, 'ExterQual'), (0.82410305288213126, 'Fireplaces'), (0.82422720251187398, 'BsmtQual'),
         (0.82430481290910129, 'LotFrontage'), (0.82435621918472424, 'BsmtCond'), (0.82454082677366924, 'RoofStyle'),
         (0.82466850644181577, 'YrSold'), (0.82487443015303608, 'YearBuilt'), (0.82501893091291767, 'YearRemodAdd'),
         (0.82541534555431062, 'Electrical'),
         (0.82647669261893386, 'PavedDrive'), (0.82655700126304987, 'Exterior1st'),
         (0.8266086111481783, 'Exterior2nd'), (0.82742038469020252, 'Foundation'), (0.82763808057540433, 'GarageArea'),
         (0.83076989529424883, 'LandSlope'), (0.83296040596747323, 'Condition2'), (0.83628884685336957, 'RoofMatl')]
    # to_drop = ['PoolQC', 'Fence', "MiscFeature", "Alley"]
    to_drop = [each[1] for each in l]
    return DropColumn(to_drop)


def get_all():
    cols = ["MSSubClass", "MSZoning", "LotFrontage", "LotArea", "Street", "Alley", "LotShape", "LandContour",
            "Utilities", "LotConfig", "LandSlope", "Neighborhood", "Condition1", "Condition2", "BldgType", "HouseStyle",
            "OverallQual", "OverallCond", "YearBuilt", "YearRemodAdd", "RoofStyle", "RoofMatl", "Exterior1st",
            "Exterior2nd", "MasVnrType", "MasVnrArea", "ExterQual", "ExterCond", "Foundation", "BsmtQual", "BsmtCond",
            "BsmtExposure", "BsmtFinType1", "BsmtFinSF1", "BsmtFinType2", "BsmtFinSF2", "BsmtUnfSF", "TotalBsmtSF",
            "Heating", "HeatingQC", "CentralAir", "Electrical", "1stFlrSF", "2ndFlrSF", "LowQualFinSF", "GrLivArea",
            "BsmtFullBath", "BsmtHalfBath", "FullBath", "HalfBath", "BedroomAbvGr", "KitchenAbvGr", "KitchenQual",
            "TotRmsAbvGrd", "Functional", "Fireplaces", "FireplaceQu", "GarageType", "GarageYrBlt", "GarageFinish",
            "GarageCars", "GarageArea", "GarageQual", "GarageCond", "PavedDrive", "WoodDeckSF", "OpenPorchSF",
            "EnclosedPorch", "3SsnPorch", "ScreenPorch", "PoolArea", "PoolQC", "Fence", "MiscFeature", "MiscVal",
            "MoSold", "YrSold", "SaleType", "SaleCondition"]
    return [DropColumn(col) for col in cols]


def get_stages():
    return [get_combined()]
