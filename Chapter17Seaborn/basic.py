import seaborn as sns
import pandas as pd
df =sns.load_dataset('titanic')
print(df.head())   
df.info()      
print(df.describe())
print(df.columns)
print(df.duplicated())
printduplicates = df.duplicated()
print("Total Duplicates: ",printduplicates.sum())
df.drop_duplicates(inplace=True)
print(f"Total Duplicates: printduplicates.sum())
print(df.isnull())
