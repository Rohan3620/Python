# WAP to show what happens when two keys having same value

my_dic = {}

# First entry
my_dic.update({"Rohan": "Hindi"})
# Second entry with same key — old value gets overwritten
my_dic.update({"Krsihna": "Hindi"})
print( my_dic)  