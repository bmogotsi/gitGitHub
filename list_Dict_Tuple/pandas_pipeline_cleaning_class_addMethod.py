# Create a Data Cleaning Pipeline
# Here’s a modular cleaning pipeline that you can customize as required:
import pandas as pd
from pandas_pipeline_cleaning_class import DataCleaningPipeline, remove_duplicates, standardize_dates, clean_text_columns, generate_quality_metrics
import sys
import pprint 

# 1989-09-20, 2010-07-18, 1969-05-26, 1999-07-09
# 'DOB':["1989-09-20 00:00:00", "2010-07-18 00:00:00", "1969-05-26 00:00:00", "1999-07-09 00:00:00"],
27, 29, 100028, 32
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj' , 'Gaurav' ],
        'numeric_columns1':[0,0,None,0 , None],
        'Address':['Delhi', 'Kanpur   ', 'Allahabad', 'Kannauj' , 'Allahabad'],
        'date_columns':["1989-09-20", "2010-07-18", "1969-05-26", "1999-07-09" , "1969-05-26"],
        'numeric_columns':[27, 100024, 100000028, 32, 100000028],
        'date2':["2025-09-20", "2010-07-18", None, "1999-07-09" , None],
        'column_aikhona':[27, 27, 100028, 32 , 100028],
        'column_aikhona':[27, 27, 100028, 32 , 100028],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd#', 'MCA']}
 
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


# And you can use the pipeline like so:
pipeline = DataCleaningPipeline()
pipeline.add_step('remove_duplicates', remove_duplicates)
pipeline.add_step('standardize_dates', standardize_dates)
pipeline.add_step('clean_text_columns', clean_text_columns)
qaMetrics = generate_quality_metrics(df)



currdf, currresult = pipeline.execute(df)

print(currdf.columns)
print(currdf.shape)
print(currdf.dtypes)
 
pprint.pprint(currdf)

print("\n+\n")
pprint.pprint(qaMetrics)
sys.exit