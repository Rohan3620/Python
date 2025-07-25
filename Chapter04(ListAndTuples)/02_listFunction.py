My_List = [0, 4, 3, 5, 2]

print("Datatype is:", type(My_List))
print("Size of list:", len(My_List))
print("First element:", My_List[0])

My_List[0] = 1
print("Updated list:", My_List)

My_List.sort()
print("Sorted list:", My_List)

My_List.append(6)
print("After append:", My_List)

My_List.insert(0, 0)
print("After insert at 0:", My_List)

My_List.reverse()
print("After reverse:", My_List)

print("Popped element at index 5:", My_List.pop(5))
print("After pop:", My_List)

My_List.remove(6)
print("After removing 6:", My_List)

b = My_List.copy()
print("Shallow copy of My_List:", b)

print("Count of 2:", My_List.count(2))
print("Index of 2:", My_List.index(2))

My_List.extend([6, 7, 8, 9])
print("Extended list:", My_List)

print("Is 2 in list:", 2 in My_List)
print("Is 100 in list:", 100 in My_List)

print("Minimum value:", min(My_List))
print("Maximum value:", max(My_List))
print("Sum of elements:", sum(My_List))

print("Range to list:", list(range(5)))
print("String to list:", list("ROhan"))

My_List.clear()
print("After clear:", My_List)

