name="Rohan is     good  boy "
print("Duoble space checking",name.find("  "))
print(name.replace("  "," "))
print("it show string are imutable ",name.find("  "))
print("Duoble space checking",name.replace("  "," ").find("  "))
cleaned = " ".join(name.split())
print(cleaned)
