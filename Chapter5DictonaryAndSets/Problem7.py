# WAP to show what happens when same key is used multiple times

my_dic = {}

# First entry
my_dic.update({"Rohan": "Hindi"})
print(my_dic)  

# Second entry with same key — old value gets overwritten
my_dic.update({"Rohan": "English"})
print("It will update the key value if having same:", my_dic)  

# If you want to store multiple values, use a list instead
my_dic["Rohan"] = ["English"]
my_dic["Rohan"].append("Hindi")  # Now you can add more languages
print("Storing multiple languages:", my_dic)  # {'Rohan': ['English', 'Hindi']}
