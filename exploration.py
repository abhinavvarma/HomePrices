import numpy
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from scikits.statsmodels.tools import categorical

df = pd.read_csv('dataset/train.csv')
#df.drop('SalePrice', axis = 1, inplace = True)
#test = pd.read_csv('../input/test.csv')
#df = df.append(test, ignore_index = True)

target_feature = "SalePrice"
target_series = df[target_feature]

for feature in df:
    print feature , "vs", target_feature
    numerical_series = categorical(df[feature], drop=True).argmax(1)
    print numpy.corrcoef(df[feature], target_series)[0, 1]

print df.describe()