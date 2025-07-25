# WAP to read the text from a given file "Poems.txt"
# and find out whether it contains the word "Twinkle"

with open("Poems.txt") as f:
    content = f.read()

print(content)

if "Twinkle" in content:
    print("Yes, 'Twinkle' is present.")
else:
    print("No, 'Twinkle' is not present.")
