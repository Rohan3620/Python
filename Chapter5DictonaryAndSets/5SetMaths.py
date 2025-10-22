s1={1,45,6,78}
s2={7,8,1,78}
sub1={1,45}
sub2={0,3,55,67}
print("Set one",s1)
print("Set two",s2)
print("Union of two sets ",s1.union(s2))
print("Intersection of two sets",s1.intersection(s2))
print("Differnce of two sets ",s1.difference(s2))
print("Differnce of two sets ",s2-s1)
print("Symmetric differnce of two sets ",s1.symmetric_difference(s2))

print("Is set subset of s1",sub1.issubset(s1))
print("Is set subset of s2",sub1.issubset(s2))
print("Is s1 superset of set",s1.issuperset(sub1))
print("Is s2 superset of set",s2.issuperset(sub1))
print("Check dijoint",sub2.isdisjoint(s1))
print("Check dijoint",sub2.isdisjoint(s2))
print("Check dijoint",sub1.isdisjoint(s1))
print("Check dijoint",sub1.isdisjoint(s2))
s1.symmetric_difference_update(s2)
print("After symmetric_difference_update:", s1)  # Output: {1, 4}

