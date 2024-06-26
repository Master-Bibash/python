fruits=["apple","banana","mango","guava","litchi"]
numbers=[1,3,6,2,9]
print(len(fruits))
print(type(fruits))

fruits2=list(("apple","banana","mango","guava","litchi"))
print(type(fruits2))
print(fruits2[-1]) ##from last element
print(fruits2[2:4])
print(fruits2[:4])
print(fruits2[-3:-2])
print(fruits2[-5:-3])


if "banana" in fruits2:
     print("yes there is banana")

fruits2[1:4]=["pineapple","orange"]
print(fruits2)
print(fruits2.insert(2, "pear"))
print(fruits2)
fruits2.append("watermelon")
print(fruits2)
fruits3=["cherry","mushrooms"]
fruits2.extend(fruits3)
print(fruits2)

fruits2.remove("apple")
print(fruits2)
fruits2.pop(1)
print(fruits2)
del fruits2[0]
print(fruits2)

newlist=["apple","orange"]
newlist.clear()
print(newlist)

vegetables=['tomato','onion']
print(vegetables[0].upper())
print(f"the next fruit is {vegetables[1]}")