##example of tupple
tupplelist=("banana","apple","orange","pear")
print(tupplelist)
maketupple = tuple(("a", "p", "b", "t")) ##touples are not changable like list
print(maketupple[0])
print(maketupple[-1])
print(maketupple[1:3])
print(maketupple[:3])
if "a" in maketupple:
     print("xa")
else:
          print("no")
         
     

print(type(tupplelist))
print(maketupple)


##lets convert tupls to list so that it can be changed
x=("man","women","god")
p=("raju",)
x+=p
y=list(x)
y.append("kala")
x=tuple(y)
print(x)
del x ##delete tuple completly

b=("bosy","giarl","cm","monk","lunk")
(boy, girl, *cm)=b
print(cm)

##loops 
mind=("ok","done","\n")
for i in mind:
     print(i)

##other method
ink=("tank","sank",'\n')
for item in range(len(ink)):
     print(ink[item])

print("----------------")
j=0
while(j<len(ink)):
     print(ink[j])
     j+=1

#add tuples
tup1=("a","b","c")
tup2=("1",2)
tup3=tup1+tup2
print(tup3)

tup4=(1,1,1,4,4,5,5,3,3,6,1)
print(tup4.count(1))
print('-------------------------------------')
<<<<<<< HEAD
print(tup4.index(5))
<<<<<<< HEAD
po,opt=(1,2)
print(po)
=======
print(tup4.index(5))
>>>>>>> 4bc496a08cf94efdc4e95a6eb4d2029e7450923f
=======
>>>>>>> 9202b6202aa509456d49f6c5f02f5c04ff129f56
