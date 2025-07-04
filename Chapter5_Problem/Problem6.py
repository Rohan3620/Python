#create empty dictionary allow 4 friend to enter their names(key) and language(values)
my_dic = {}
for i in range(4):
   name=input("Enter name of user ")
   language=input("Enter language of user ")
#    my_dic.update({name:language})
   if name in my_dic:
        my_dic[name] += ", " + language  # Add new language if name already exists
   else:
        my_dic[name] = language

print(my_dic)   