# Create a Data Cleaning Pipeline
# Here’s a modular cleaning pipeline that you can customize as required:
import pandas as pd
class DataCleaningPipeline:
    """
    A modular pipeline for cleaning data with customizable steps.
    """
    
    def __init__(self):
        self.steps = []
        
    def add_step(self, name, function):
        """Add a cleaning step."""
        self.steps.append({'name': name, 'function': function})
        
    def execute(self, df):
        """Execute all cleaning steps in order."""
        results = []
        current_df = df.copy()
        
        for step in self.steps:
            try:
                current_df = step['function'](current_df)
                results.append({
                    'step': step['name'],
                    'status': 'success',
                    'rows_affected': len(current_df)
                })
            except Exception as e:
                results.append({
                    'step': step['name'],
                    'status': 'failed',
                    'error': str(e)
                })
                break
                
        return current_df, results

# You can then define functions to add data cleaning steps:
def remove_duplicates(df):
    return df.drop_duplicates() # drop duplicate ROWS not columns

def standardize_dates(df):
    date_columns = df.select_dtypes(include=['datetime64']).columns #d fffff
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

# Automate String Cleaning and Standardization
#           capitalization       = lower
#           extra spaces         = remove
#           special characters   = remove   
def clean_text_columns(df, columns=None):
    """
    Apply standardized text cleaning to specified columns.
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (list): List of columns to clean. If None, clean all object columns
    
    Returns:
        pd.DataFrame: Dataframe with cleaned text columns
    """
    if columns is None:
        columns = df.select_dtypes(include=['object']).columns
        
    df = df.copy()
    
    for column in columns:
        if column not in df.columns:
            continue
            
        # Apply string cleaning operations
        df[column] = (df[column]
                     .astype(str)
                     .str.strip()
                     .str.lower()
                     .replace(r'\s+', ' ', regex=True)  # Replace multiple spaces: \s(space) +()
                     .replace(r'[^\w\s]', '', regex=True))  # Remove special characters:  ^(Not) \w(a-zA-Z0-9_) word characters \s(space)
                     
    return df


# Monitor Data Quality Over Time
# The monitoring function below helps you track key quality metrics
# and identify potential issues before they become problems: 

def generate_quality_metrics(df, baseline_metrics=None):
    """
    Generate quality metrics for a dataset and compare with baseline if provided.
    
    Args:
        df (pd.DataFrame): Input dataframe
        baseline_metrics (dict): Previous metrics to compare against
        
    Returns:
        dict: Current metrics and comparison with baseline
    """
    metrics = {
        'row_count': len(df),
        'missing_values': df.isna().sum().to_dict(),
        'unique_values': df.nunique().to_dict(),
        'data_types': df.dtypes.astype(str).to_dict()
    }
    
    # Add descriptive statistics for numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns
    metrics['numeric_stats'] = df[numeric_columns].describe().to_dict()
    
    # Compare with baseline if provided
    if baseline_metrics:
        metrics['changes'] = {
            'row_count_change': metrics['row_count'] - baseline_metrics['row_count'],
            'missing_values_change': {
                col: metrics['missing_values'][col] - baseline_metrics['missing_values'][col]
                for col in metrics['missing_values']
            }
        }
    
    return metrics


abc ="width Length hEiGhT"
print(abc)
print("lower....:" + abc.lower())
print("Capitalize....:" + abc.capitalize())
print("casefold....:" + abc.casefold())
print("title....:" + abc.title())
print("UPPER....:" + abc.upper())