list=[1,2,3,4,5,6]
for i in range(len(list)):
     if list[i]%2!=0:
          print(list[i])

for i in range(4,0,-1):
     print(i)


person={
     "name":"Avisek",
     "age":19,
     "num":[1,2,3,4,5,6,10],
}

for key,value in person.items():
     # print(key,value)
     if key=="num":
          for i in range(len(value)):
               print(value[i])
               if value[i]%2!=0:
                    print(i)


for i in range(10):
     for m in range(10):
         print('*',end=''),
     print()
