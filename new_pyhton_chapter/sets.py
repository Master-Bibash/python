<<<<<<< HEAD
<<<<<<< HEAD
firstset={"ant","ball","cat","ant"}
=======
firstset = {"ant", "ball", "cat", "ant"}
>>>>>>> 9202b6202aa509456d49f6c5f02f5c04ff129f56
print(firstset)
=======
firstset={"ant","ball","cat"}
>>>>>>> 4bc496a08cf94efdc4e95a6eb4d2029e7450923f
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
<<<<<<< HEAD
<<<<<<< HEAD
newset2={"a","m","p","sigma","a"}
print(newset2)
=======
newset2={"a","m","p","sigma"}
>>>>>>> 4bc496a08cf94efdc4e95a6eb4d2029e7450923f
set3=newset.union(newset2)
set4=newset.intersection(newset2) ## only keep dulpcated
set5=newset.intersection_update(newset2)
print(set4)
print(set3)
print(set5)
<<<<<<< HEAD

print("-----------------------")
newz={1,True,False,0}
print(newz)
=======
>>>>>>> 4bc496a08cf94efdc4e95a6eb4d2029e7450923f
=======
newset2 = {"a", "m", "p", "sigma"}
set3 = newset.union(newset2)
set4 = newset.intersection(newset2)  # only keep dulpcated
set5 = newset.intersection_update(newset2)
print(set4)
print(set3)
print(set5)
>>>>>>> 9202b6202aa509456d49f6c5f02f5c04ff129f56
