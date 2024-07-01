def my_fun(name,age):
     print(f" name is {name} and age is {age}")

my_fun("bibash",12)

#use * if the number of arguments are unknown
def find(*values):
     print(f"number two is {values[0]}")

find("a","p","m")

#pass key value pairs
def next_fun(child1,child2,child3):
     print("second son is "+child2)
next_fun(child1="ramu", child2="babu", child3="lala")

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** 
def next_fun2(**names):
     print(" his second son is "+names["seckid"])


next_fun2(fname="raju", seckid="papu",third="kala")

#deafult
def value_default(age=22):
     print("I am "+age.__str__() )
value_default()

def addition(a,b):
     return a+b
print(addition(1, 5))

def nothing(num):
     pass
nothing(3)

#only make sure it takes one argument
def anotherone(x,/):
     print(x)
anotherone(212,)

def anotherone2(x):
     print(x)
anotherone2(x=3)

# To specify that a function can have only keyword arguments, add *, before the arguments:
def anotherone3(*,x):
     print(x)
anotherone3(x=200) ## value showuld be given like this x=20 not (20)

#so any argument befire / is positoinal (2) and after * is keyword-only (a=4)

def anotheronw4(a,b,c,/,*,d,e,f):
     print(a,b,c,d,e,f)

anotheronw4(1,2,4,d=4,e=6,f=5)

#find recursion

def find_recur(j):
     if (j>0):
          recurSum=j+find_recur(j-1)
     else:
         recurSum = 0
     return recurSum


print(f"final recursion is {find_recur(6)}")
