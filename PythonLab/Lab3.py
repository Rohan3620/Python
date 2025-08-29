n = int(input("Enter numbers : "))

count = 0  
sum = 0 
num = 2 

while count < n:
    flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break
    if flag==True:
        sum += num
        count += 1
    num += 1

print(f"Sum of first {n} prime numbers is= {sum}")
