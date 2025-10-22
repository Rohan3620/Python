# A spam comment is defined as a text containing any of the following keywords

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter a comment: ").lower().strip()  # Convert to lowercase & remove extra spaces

if p1 in message or p2 in message or p3 in message or p4 in message:
    print("🚨 Alert: Spam detected!")
else:
    print("✅ This is a clean message:", message)
