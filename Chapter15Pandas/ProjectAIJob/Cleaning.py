import pandas as pd
df = pd.read_csv(r"C:\Users\C9IN\Desktop\coding\Python\Chapter15Pandas\Data\ai_job_dataset.csv")
print("Total duplicated values before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Total duplicated values after:", df.duplicated().sum())
print("Total null values before:\n", df.isnull().sum())
salary_mean = df['salary_usd'].mean()
df['salary_usd'] = df['salary_usd'].fillna(salary_mean)
print("Total null values after:\n", df.isnull().sum())
df.rename(columns={"salary_usd": "salary"}, inplace=True)
print(df["salary"])
df['bonus'] = df['salary'] * 2
print(df["bonus"])

