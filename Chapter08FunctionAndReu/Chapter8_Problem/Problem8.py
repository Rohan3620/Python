def functionremove(l, word):
    # Remove all occurrences of `word`
    return [item for item in l if item != word]

def functionstrip(l, word):
    # Strip `word` from both ends of each item (like strip("Rohan"))
    return [item.strip(word) for item in l]

# Main Code
my_list = []
for i in range(5):
    element = input("Enter element of list: ")
    my_list.append(element)

print("Original List:", my_list)

# Step 1: Remove 'Rohan'
cleaned_list = functionremove(my_list, "Rohan")
print("After Removing 'Rohan':", cleaned_list)

# Step 2: Strip 'Rohan' from each element
stripped_list = functionstrip(cleaned_list, "Rohan")
print("After Stripping 'Rohan' from elements:", stripped_list)
