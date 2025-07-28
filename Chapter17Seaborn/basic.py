import seaborn as sns
import pandas as pd
df =sns.load_dataset('titanic')
print(df.head())   
df.info()      
print(df.describe())
print(df.columns)
null=df.isnull()
print("Total number of null\n",null.sum())
print(df["deck"].value_counts())
printduplicates = df.duplicated()
print(f"Total Duplicates: {printduplicates.sum()}")
