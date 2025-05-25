
# Import pandas package
import pandas as pd
 
# Define a dictionary containing employee data
data1 ={'Name':['jai', 'princi pine', 'gaurav Botha', 'Anuj south']}
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name', 'Age', 'Address', 'Qualification']])

names = pd.DataFrame(data1)
names['Name'] = names['Name'].str.title()
print(names)
print(str(names).str.title() + "01")
