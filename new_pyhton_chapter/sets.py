firstset = {"ant", "ball", "cat", "ant"}
print(firstset)
print(len(firstset))
print("ant" not in firstset)
secondset = {"alt", "and", "ball"}
thirdlist = [1, 24]
firstset.update(secondset)
firstset.update(thirdlist)
firstset.remove(24)
firstset.discard(24)
# firstset.remove(24) ##throws an error
firstset.pop()  # removes random items
firstset.clear()

print(firstset)
print("--------------------------------")
newset = {"lamda", "sigma", "pigma"}
# del newset
newset2 = {"a", "m", "p", "sigma"}
set3 = newset.union(newset2)
set4 = newset.intersection(newset2)  # only keep dulpcated
set5 = newset.intersection_update(newset2)
print(set4)
print(set3)
print(set5)
