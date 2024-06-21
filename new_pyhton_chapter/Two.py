a="""This is  a miltiline comment lorem128sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"""
print(a)

b='''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
'''
print(b)
##lets do string slicing
s=" biBash karki"
print(s[0:4]) ## from 0 to 4 where 4 is not included
print(s[1:]) ## 1: means it will print from 1 not from 0
# print(s[-4,-2]) ## throws exception

print(s.upper()) ##to uppercase
print(s.lower()) ##to lowercase
print(s.strip())  ##deletes the white space
print(s.replace("i", "A")) ## replaces the string
print(s.split(",")) ## it splits the string ana makes the list

test="bibash, is a specialkid"
print(test.split(","))
print(len(test.split(","))) ##length starts from 1 and index starts from 0

##lets concanite the string
name="bibash"
caste="karki"
print(name+" "+caste)

print("my name is "+name+"and caste is "+caste)
print(f"my name is {name} and caste is {caste}")
paisa=40
print(f"ani kati vayo {paisa:.2f} dollers")

print("this is my name \"bibash\" and hi")

print("the center is ")
