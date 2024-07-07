dictname={
     "ram":67,
     "shyma":65,
     "haru":88,
     "ramesh":12
}
name = input("enter name ").lower()
if name.lower() in dictname:
    print(f"hi {name} your grade is {dictname[name] }")
else:
     print("name not found")
print("--------------------------------")
