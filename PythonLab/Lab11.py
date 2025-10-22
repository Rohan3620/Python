l = [1, 2, 3, 4, 5, 6, 7, 8]
n = int(input("Enter a number to search: "))

for i in l:
    if i == n:
        print(f"{n} is found in list")
        break
else:
    print(f"{n} is not found in list")


