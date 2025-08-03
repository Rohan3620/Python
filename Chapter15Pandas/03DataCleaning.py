import pandas as pd

# Load the CSV file
df = pd.read_csv(r"C:\Users\C9IN\Downloads\Data\mtcars2.csv")

# Display original data
print("Original DataFrame:")
print(df)

# Temporary drop of 'S.No' column
print("\nTemporary drop of 'S.No' column:")
print(df.drop(columns=['S.No']).head())

# Permanent drop of 'S.No' column
df.drop(columns=["S.No"], inplace=True)
print("\nAfter permanently dropping 'S.No' column:")
print(df.head())

# Rename column
df.rename(columns={"Unnamed: 1": "Name"}, inplace=True)
print("\nAfter renaming 'Unnamed: 1' to 'Name':")
print(df.head())

# Check duplicate rows
print("\nCheck duplicated rows (True means duplicate):")
print(df.duplicated())

# Drop duplicate rows temporarily
print("\nDataFrame after dropping duplicates (temporary):")
print(df.drop_duplicates().head())

# Count of duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Check for null values
print("\nNull values in each cell (first 5 rows):")
print(df.isnull().head())

print("\nTotal null values in each column:")
print(df.isnull().sum())

# Calculate median of 'qsec' column and fill nulls with it
x = df.qsec.median()
print(f"\nMedian of qsec: {x}")

print("\nDataFrame after filling nulls in 'qsec' with median (temporary):")
print(df.qsec.fillna(x).head())
df.qsec.fillna(x, inplace=True)

""" 
1. do the sorting of qsec column in descending order.
2. i want to filter the data for drat whose value is greater than 4.5.
3. i want to filter the data where gear is greater than 3 and car is greater than two.
4. i want to change a value of a particular column named as gear 5
5. i want to change a particular value in gear column whose row index as 10 and change the value as 500
 
"""
print(df['qsec'].sort_values(ascending=False))
print(df[df['drat'] > 4.5])
print(df[(df['gear'] > 3) & (df['carb'] > 2)])


df['gear'] = 5
print(df.head())
df.at[10, 'gear'] = 500
print(df.head())

#Drop on the basic of email same
# def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # customers = customers.drop_duplicates(subset="email")
    # return customers
df.rename(columns={"carb": "carburetor"}, inplace=True)
print(df.head())