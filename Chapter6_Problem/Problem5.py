# WAP to check if the username contains less than 10 characters

username = input("Enter the username: ")

if len(username) < 10:
    print(f"✅ Username is less than 10 characters (Size: {len(username)})")
else:
    print(f"❌ Username is 10 or more characters (Size: {len(username)})")
