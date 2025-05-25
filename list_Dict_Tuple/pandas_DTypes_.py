# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html

# To select all numeric types, use np.number or 'number'
# To select strings you must use the object dtype, but note that this will return all object dtype columns
# See the numpy dtype hierarchy
# To select datetimes, use np.datetime64, 'datetime' or 'datetime64'
# To select timedeltas, use np.timedelta64, 'timedelta' or 'timedelta64'
# To select Pandas categorical dtypes, use 'category'
# To select Pandas datetimetz dtypes, use 'datetimetz' or 'datetime64[ns, tz]'

import pandas as pd
import sys

from sklearn.impute import SimpleImputer

def handle_missing_values(df):
    # Handle numeric columns
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_columns) > 0:
        num_imputer = SimpleImputer(strategy='median')
        df[numeric_columns] = num_imputer.fit_transform(df[numeric_columns])
    
    # Handle categorical columns
    categorical_columns = df.select_dtypes(include=['object'], exclude=['bool']).columns
    if len(categorical_columns) > 0:
        cat_imputer = SimpleImputer(strategy='most_frequent')
        df[categorical_columns] = cat_imputer.fit_transform(df[categorical_columns])
    
    return df

df = pd.DataFrame({'a': [1, 2, None] * 3,
                   'b': [True, False, False] * 3,
                   'c': [1.0, 2.0, 3.0] * 3,
                   'd': ['ABC', 'XYZ', 'EFG'] * 3})

# df['d'].replace('None', '')
df['d'].fillna('').astype(str)
if True==False:
    pass
else:
    print(df)

print(df.info())
print(df.describe())


if True==True:
    #
    # Impute Data
    #################
    impute_df=handle_missing_values(df)
    print(impute_df)
    pass
else:


    #
    # Select Boolean
    ####################

    print(df.select_dtypes(include='bool'))

    print(df.describe())

    df.dropna(inplace=True) # Removing Missing Values (Remove any row with a missing value [None] on any column)
    print(df)
    
    sys.exit
