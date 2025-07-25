name="rohan"
print(len(name))
print(name.endswith("an"))
print(name.startswith("Ro"))
print(name.capitalize());
print(name.title());
print(name.lower());
print(name.upper());
print(name.find("R"));
print(name.replace("R","M"));
name=" Rohan "
print(name.strip())
print(name.lstrip())
print(name.rstrip())
name="Rohan ,Krishna ,Amit"
print(name.split(","))
print(name.swapcase())
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.isspace())
print(name.zfill(30))
lst=["Rohan","is",'Good']
print(" ".join(lst))