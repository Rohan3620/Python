import pandas as pd
df=pd.read_csv(r"C:\Users\C9IN\Desktop\coding\Python\Chapter15Pandas\ProjectAIJob\Data\ai_job_dataset.csv")
print(df.head())   
df.info()      
print(df.describe())
print(df.columns)
print(
df.isnull())
df['posting_date'] = pd.to_datetime(df['posting_date'])
df['application_deadline'] = pd.to_datetime(df['application_deadline'])

duplicates = df.duplicated()
print(f"Total Duplicates: {duplicates.sum()}")

df['job_title'] = df['job_title'].str.strip().str.lower()
df['company_name'] = df['company_name'].str.strip().str.title()  # Capitalize like "Smart Analytics"
df['industry'] = df['industry'].str.strip().str.lower()

df.to_csv('cleaned_ai_jobs.csv', index=False)





