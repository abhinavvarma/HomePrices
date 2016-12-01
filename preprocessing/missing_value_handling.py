from utils import Stage


class MeaningfulNAs(Stage):
    def run(self, all_data):
        all_data.loc[all_data.Alley.isnull(), 'Alley'] = 'NoAlley'
        all_data.loc[all_data.MasVnrType.isnull(), 'MasVnrType'] = 'None'  # no good
        all_data.loc[all_data.MasVnrType == 'None', 'MasVnrArea'] = 0
        all_data.loc[all_data.BsmtQual.isnull(), 'BsmtQual'] = 'NoBsmt'
        all_data.loc[all_data.BsmtCond.isnull(), 'BsmtCond'] = 'NoBsmt'
        all_data.loc[all_data.BsmtExposure.isnull(), 'BsmtExposure'] = 'NoBsmt'
        all_data.loc[all_data.BsmtFinType1.isnull(), 'BsmtFinType1'] = 'NoBsmt'
        all_data.loc[all_data.BsmtFinType2.isnull(), 'BsmtFinType2'] = 'NoBsmt'
        all_data.loc[all_data.BsmtFinType1 == 'NoBsmt', 'BsmtFinSF1'] = 0
        all_data.loc[all_data.BsmtFinType2 == 'NoBsmt', 'BsmtFinSF2'] = 0
        all_data.loc[all_data.BsmtFinSF1.isnull(), 'BsmtFinSF1'] = all_data.BsmtFinSF1.median()
        all_data.loc[all_data.BsmtQual == 'NoBsmt', 'BsmtUnfSF'] = 0
        all_data.loc[all_data.BsmtUnfSF.isnull(), 'BsmtUnfSF'] = all_data.BsmtUnfSF.median()
        all_data.loc[all_data.BsmtQual == 'NoBsmt', 'TotalBsmtSF'] = 0
        all_data.loc[all_data.FireplaceQu.isnull(), 'FireplaceQu'] = 'NoFireplace'
        all_data.loc[all_data.GarageType.isnull(), 'GarageType'] = 'NoGarage'
        all_data.loc[all_data.GarageFinish.isnull(), 'GarageFinish'] = 'NoGarage'
        all_data.loc[all_data.GarageQual.isnull(), 'GarageQual'] = 'NoGarage'
        all_data.loc[all_data.GarageCond.isnull(), 'GarageCond'] = 'NoGarage'
        all_data.loc[all_data.BsmtFullBath.isnull(), 'BsmtFullBath'] = 0
        all_data.loc[all_data.BsmtHalfBath.isnull(), 'BsmtHalfBath'] = 0
        all_data.loc[all_data.KitchenQual.isnull(), 'KitchenQual'] = 'TA'
        all_data.loc[all_data.MSZoning.isnull(), 'MSZoning'] = 'RL'
        all_data.loc[all_data.Utilities.isnull(), 'Utilities'] = 'AllPub'
        all_data.loc[all_data.Exterior1st.isnull(), 'Exterior1st'] = 'VinylSd'
        all_data.loc[all_data.Exterior2nd.isnull(), 'Exterior2nd'] = 'VinylSd'
        all_data.loc[all_data.Functional.isnull(), 'Functional'] = 'Typ'
        all_data.loc[all_data.SaleCondition.isnull(), 'SaleCondition'] = 'Normal'
        all_data.loc[all_data.SaleCondition.isnull(), 'SaleType'] = 'WD'
        all_data.loc[all_data['PoolQC'].isnull(), 'PoolQC'] = 'NoPool'
        all_data.loc[all_data['Fence'].isnull(), 'Fence'] = 'NoFence'
        all_data.loc[all_data['MiscFeature'].isnull(), 'MiscFeature'] = 'None'
        all_data.loc[all_data['Electrical'].isnull(), 'Electrical'] = 'SBrkr'
        # only one is null and it has type Detchd
        all_data.loc[all_data['GarageArea'].isnull(), 'GarageArea'] = all_data.loc[
            all_data['GarageType'] == 'Detchd', 'GarageArea'].mean()
        all_data.loc[all_data['GarageCars'].isnull(), 'GarageCars'] = all_data.loc[
            all_data['GarageType'] == 'Detchd', 'GarageCars'].median()
        return all_data


def get_stages():
    return [MeaningfulNAs]