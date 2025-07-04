#WAP to input eight nummber from the user and display all the unique number(Once)
my_set = set()
for i in range(8):
    word = int(input(f"Enter a {i+1} number : "))  # User se number input liya
    my_set.add(word)  # Set me number add kiya (duplicate auto remove ho jayega)
print(my_set)
  