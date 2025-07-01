#WAP to create a dicitioary of hindi to english.
#Provide user with an option to look it up 
dic = {
    "aam": "Mango",
    "paani": "Water",
    "dost": "Friend",
    "kitab": "Book",
    "ghar": "Home",
    "khaana": "Food",
    "gaadi": "Car",
    "ladki": "Girl",
    "suraj": "Sun",
    "chand": "Moon"
}

# Sabhi available hindi words ko show karwa rahe ha
print("Available Hindi words:", list(dic.keys()))

# User se hindi word lene ke liye input le rahe ha aur use lowercase me convert kar rahe ha
word = input("Enter the Hindi word to find its English meaning: ").lower()

# Dictionary me user ka word check kar rahe ha aur uska meaning la rahe ha
meaning = dic.get(word)

# Agar meaning mila toh print karenge
if meaning:
    print("Meaning is:", meaning)
# Agar word dictionary me nhi mila toh ye print hoga
else:
    print("Sorry, word not found in dictionary.")
