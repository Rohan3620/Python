import pandas as pd
Data=pd.read_csv(r"C:\Users\C9IN\Desktop\coding\Python\Chapter15Pandas\Data\salaries.csv")
print(Data[Data["experience_level"]=='SE'])
print(Data[Data["company_location"].isin(['GB', 'LT'])])
print(Data[Data["salary"]>100000])
print(Data[(Data["experience_level"] == 'SE') & (Data["salary"] > 150000)])
print(Data.sort_values(by="salary", ascending=False).head(5))
filtered = Data[Data["salary"] > 100000]
print("Number of rows with salary > 100000:", len(filtered))
