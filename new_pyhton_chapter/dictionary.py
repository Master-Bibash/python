mydict={
     "name":"bibash",
     "caste":"karki",
     "age":20,
     "height":5.6,
     "weight":60,
     "address":"kathmandu",
     "phone":9876543210,
     "email":"bibash.com"
}
print(len(mydict.items()))
print(mydict.get("email"))
print(mydict.keys())
mydict['address']="sindhuli"
print(mydict.values())
print(mydict.items())


#check values
if "names" in mydict:
     print("eys")

print(mydict.update({"name":"bibash karki"}))
mydict.pop("age")
mydict.popitem() ##removes last item
print(mydict)
print("--------------------------------")
newdict={
     "name":"Raj",
     "caste":"kami",
     "age":25,
     "height":9.6,
     "weight":80,
     "address":"palpa",
     "phone":987654320,
     "email":"nope.com"
}
newdict2=newdict.copy()
newdict.popitem()
print(newdict)
print(dict(newdict))
print(newdict2)

print('-----------------------------')
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily["child1"]["name"])

for x,obj in myfamily.items():
     print(x)
     for y in obj:
          print(y+" ",obj[y])
