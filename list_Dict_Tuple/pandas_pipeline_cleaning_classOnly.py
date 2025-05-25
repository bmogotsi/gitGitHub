# Create a Data Cleaning Pipeline
# Here’s a modular cleaning pipeline that you can customize as required:
import sys, pandas as pd
import pprint

"""
Implement Automated Data Validation
 """
# validate 
#       valid date range 
#       Numbers only - no Strings in column (int only)
def validate_dataset(df, validation_rules=None):
    """
    Apply validation rules to a dataframe and return validation results.
    
    Args:
        df (pd.DataFrame): Input dataframe
        validation_rules (dict): Dictionary of column names and their validation rules
        
    Returns:
        dict: Validation results with issues found
    """
    import pandas as pd

    # First, we define the validation rules:
    if validation_rules is None:
        validation_rules = {
            'numeric_columns': {
                'check_type': 'numeric',
                'min_value': 0,
                'max_value': 1000000
            },
            'numeric_columns1': {
                'check_type': 'numeric',
                'min_value': 0,
                'max_value': 1000000
            },
            'date_columns': {
                'check_type': 'date',
                'min_date': '2000-01-01',
                'max_date': '2025-12-31'
            },
            'date2': {
                'check_type': 'date',
                'min_date': '2000-01-01',
                'max_date': '2025-12-31'
            }
        }

    # apply the checks and return the results:
        validation_results = {}
    
    issues = []
    for column, rules in validation_rules.items():
        if column not in df.columns:
            continue
            
        issues = []
        
        # Check for missing values
        missing_count = df[column].isna().sum() # None keyword is used to represent missing data
        if missing_count > 0:
            issues.append(f"Found {missing_count} missing values")
            
        # Type-specific validations
        if rules['check_type'] == 'numeric':
            if not pd.api.types.is_numeric_dtype(df[column]):
                issues.append("Column should be numeric")
            else:
                out_of_range = df[
                    (df[column] < rules['min_value']) | 
                    (df[column] > rules['max_value'])
                ]
                if len(out_of_range) > 0:
                    issues.append(f"Found {len(out_of_range)} values outside allowed range")
           
        
        # Check Date
        if rules['check_type'] == 'date':
            if not pd.api.types.is_datetime64_any_dtype(df[column]):
                issues.append("Column should be a date")
            else:
                out_of_range = df[
                    (df[column] < rules['min_date']) | 
                    (df[column] > rules['max_date'])
                ]
                if len(out_of_range) > 0:
                    issues.append(f"Found {len(out_of_range)} values outside allowed range")

        validation_results[column] = issues
    
    return validation_results

from datetime import datetime, timedelta, date
date = datetime.now()
# 1989-09-20, 2010-07-18, 1969-05-26, 1999-07-09
# 'DOB':["1989-09-20 00:00:00", "2010-07-18 00:00:00", "1969-05-26 00:00:00", "1999-07-09 00:00:00"],
27, 29, 100028, 32
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'numeric_columns1':[0,0,None,0],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'date_columns':["1989-09-20", "2010-07-18", "1969-05-26", "1999-07-09"],
        'numeric_columns':[27, 100024, 100000028, 32],
        'date2':["2025-09-20", "2010-07-18", None, "1999-07-09"],
        'column_aikhona':[27, 29, 100028, 32],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
# Initial cleaning steps
df.columns = df.columns.str.strip().str.lower()  # Standardize column names
df = df.replace('', pd.NA)  # Convert empty strings to NA

# chnage to date type
# df.astype({'DOB': 'datetime64[ns]'})
df['date_columns'] = pd.to_datetime(df['date_columns'])
df['numeric_columns'] = pd.to_numeric(df['numeric_columns'])
df['date2'] = pd.to_datetime(df['date2'])
df['numeric_columns1'] = pd.to_numeric(df['numeric_columns1'])
df['column_aikhona'] = pd.to_numeric(df['column_aikhona'])

print(df.columns)
print(df.shape)
print(df.dtypes)
 
print(df)

validOrNot = validate_dataset(df,None)
#print(validOrNot)
pprint.pprint(validOrNot)
sys.exit
 