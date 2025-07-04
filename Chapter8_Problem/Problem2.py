#WAP using fuction covert celsuis to fahrenhiet
def convertor(c):
    f = (c * 9 / 5) + 32
    return f

c = float(input("Enter temperature in Celsius: "))
fahrenheit = convertor(c)
print(f"Temperature in Celsius {c}°C is {fahrenheit:.2f}°F")
