"""  
it is an open source library 
pandas -panel + data +s 
we deal with series and data frame 
-slicing,indexing,sorting,filtering,renaming,
filling the null values ,iloc/ioc
"""
# Series : it consist od one dimensional data 
import pandas as pd
a=pd.Series([10,20,30,40])
print(a)
print()
a=pd.Series([10,20.0,30,40])
print(a)
print()
a=pd.Series([10,"20",30,40])
print(a)
print()
print("Change indexing ")
a=pd.Series([10,"20",30,40],index=['a','b','c','d'])
print(a)
print()
a=pd.Series([10,"20",30,40],index=range(1,5))
print(a)
print()
a=pd.Series([[1,"Rohan"],
            [2,"Rohit"],
            [3,"Ravi"],
            [4,"Ram"]]
            )
print(a)
print()
# dataframe : it is series of 2D data
print("Data Frames")
print()
a=pd.DataFrame([[1,"Rohan"],[2,"Rohit"],[3,"Ravi"],[4,"Ram"]])
print(a)
print()
# make series with help of list for 5 company name ,loc
a=pd.Series([["Google","Noida"],["HCL","Delhi"],["Tata","Noida sec63"],["Adobe","Noida sec62"],["ISEGEC","Delhi"]])
print(a)
print()
# make datframe for 10student, name, there total marks ,section,courese,sem

a=pd.DataFrame([
    ["Rohan",100,"E1","BCA",3],
    ["Rohit",90,"E2","B.com",4],
    ["Ravi",70,"M1","BCA",2],
    ["Ram",89,"E1","BBA",2],
    ["Shyam",100,"E1","BCA",6],
    ["Shubam",90,"E2","B.com",4],
    ["Narayan",70,"M1","BCA",2],
     ["Amit",89,"E1","BBA",2],
     ["Krishna",70,"M1","BCA",2],
  ["Rushali",89,"E1","BBA",2],
    ],columns=["Name","Marks","Section","Course","Semester"],index=range(1,11))
print(a)
print()