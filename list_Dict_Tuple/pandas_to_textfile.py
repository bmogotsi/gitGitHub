

import pandas as pd
#specify path for export
path ="pandas_textfile.text"

# 
df = pd.read_html("sample_html.html") # no table

#export DataFrame to text file
with open(path, 'a') as f:
    df_string = df.to_string(header=False, index=False)
    f.write(df_string)