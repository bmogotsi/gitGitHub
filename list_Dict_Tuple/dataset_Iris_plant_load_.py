# https://www.kdnuggets.com/data-cleaning-with-pandas
import pandas as pd


column_names = [  'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
#iris_data = pd.read_csv('data/iris.csv', names= column_names, header=None)
iris_data = pd.read_csv('data/iris.data', names= column_names, header=None)
print(iris_data.head())

print(iris_data.shape)

# print(iris_data)

# 2. Explore the dataset
print(iris_data.info())         # column data types and memory usage
print(iris_data.describe())     # summary descriptive statistics of a DataFrame
#pd.read('data/iris.data', names= column_names, header=None)


# 3. Checking Class Distribution
print(iris_data['species'].value_counts())

# 4. Removing Missing Values
iris_data.dropna(inplace=True)

duplicate_rows = iris_data.duplicated()
print("Number of duplicate rows:", duplicate_rows.sum())

# 6. One-Hot Encoding
encoded_species = pd.get_dummies(iris_data['species'], prefix='species', drop_first=False).astype('int')
iris_data = pd.concat([iris_data, encoded_species], axis=1)
iris_data.drop(columns=['species'], inplace=True)


# 7. Normalization of Float Value Columns
# Normalization is the process of scaling numerical features to have a mean of 0 and a standard deviation of 1. 
# This process is done to ensure that the features contribute equally to the analysis. 
# We will normalize the float value columns for consistent scaling
#from scikit-learn.preprocessinb
#import scikit-learn
#import scikit
from sklearn import preprocessing

# Normalization of Float Value Columns
# process of scaling numerical features to have a mean of 0 and a standard deviation of 1. 
# This process is done to ensure that the features contribute equally to the analysis.
scaler = preprocessing.StandardScaler()
cols_to_normalize = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
scaled_data = scaler.fit(iris_data[cols_to_normalize])
iris_data[cols_to_normalize] = scaler.transform(iris_data[cols_to_normalize])

# Dataset Insight
print(iris_data.info())         # column data types and memory usage
print(iris_data.describe())     # summary descriptive statistics of a DataFrame

# 8. Save the cleaned dataset
# Save the cleaned dataset to the new CSV file.

iris_data.to_csv('cleaned_iris.csv', index=False)