def table(n): 
    print(f"Table of {n:<10} Reverse Table of {n}:\n")
    for i in range(1, 11):
        normal = f"{n} * {i:<2} = {n*i:<3}"
        reverse = f"{n} * {11-i:<2} = {n*(11-i):<3}"
        print(f"{normal}        {reverse}")

number = int(input("Enter a number: "))
table(number)
""" 
| Part | Meaning                           |
| ---- | --------------------------------- |
| `n`  | The **value** you're inserting    |
| `:`  | Introduces a **format specifier** |
| `<`  | **Left-align** the value          |
| `15` | Use a **width of 15 characters**  |
| Format    | Description               | Example Output |
| --------- | ------------------------- | -------------- |
| `{x:<10}` | Left-align in 10 spaces   | `x       `     |
| `{x:>10}` | Right-align in 10 spaces  | `       x`     |
| `{x:^10}` | Center-align in 10 spaces | `   x    `     |



"""