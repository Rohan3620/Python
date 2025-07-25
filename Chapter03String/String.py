name = "Rohan Mishra"
Fname = name[0:5]             # Takes characters from index 0 to 4 → 'Rohan'
a = len(name)
print(name + " Length of String : ", a)   # Full name + length (12)

a = len(Fname)
print(Fname + " Length of String : ", a)  # Fname ('Rohan') + length (5)

Fname = name[-5:-1]           # Takes characters from index -5 to -2 → 'ishr'
a = len(name)
print(Fname + " Length of String : ", a)  # Fname ('ishr') + full length again (12)
