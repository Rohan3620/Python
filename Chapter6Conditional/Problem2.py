# WAP to find greatest of four numbers entered by the user

numbers = []
for i in range(4):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

print("Numbers entered:", numbers)

greatest = numbers[0]
for num in numbers:
    if num > greatest:
        greatest = num

print("Greatest number out of four is:", greatest)
