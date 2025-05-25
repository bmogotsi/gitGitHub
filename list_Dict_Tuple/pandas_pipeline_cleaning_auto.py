# Reproducible Pipeline - Automate Data Cleaning

import pandas as pd

# Step 1: Run Basic Data Quality Checks
def check_data_quality(df):
    # Store initial data quality metrics
    quality_report = {
        'missing_values': df.isnull().sum().to_dict(),
        'duplicates': df.duplicated().sum(),
        'total_rows': len(df),
        'memory_usage': df.memory_usage().sum() / 1024**2  # in MB
    }
    return quality_report

# Step 2: Standardize Data Types
# This step prevents type-related errors in subsequent analysis.
def standardize_datatypes(df):
    for column in df.columns:
        # Try converting string dates to datetime
        if df[column].dtype == 'object':
            try:
                df[column] = pd.to_datetime(df[column]) # The default return dtype is float64 or int64 depending on the data supplied. 
                print(f"Converted {column} to datetime")
            except ValueError:
                # Try converting to numeric if datetime fails
                try:
                    df[column] = pd.to_numeric(df[column].str.replace('$', '').str.replace(',', '')) # The default return dtype is float64 or int64 depending on the data supplied. 
                    print(f"Converted {column} to numeric")
                except:
                    pass
    return df

# Step 3: Handle Missing Values
# Missing values can significantly impact our analysis. Rather than dropping data records with missing values, we can use imputation strategies:
#       Using median imputation for numeric columns
#       Applying mode imputation for categorical data
#       Maintaining the statistical properties of the dataset while filling gaps 

from sklearn.impute import SimpleImputer

def handle_missing_values(df):
    # Handle numeric columns
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_columns) > 0:
        num_imputer = SimpleImputer(strategy='median')
        df[numeric_columns] = num_imputer.fit_transform(df[numeric_columns])
    
    # Handle categorical columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    if len(categorical_columns) > 0:
        cat_imputer = SimpleImputer(strategy='most_frequent')
        df[categorical_columns] = cat_imputer.fit_transform(df[categorical_columns])
    
    return df


