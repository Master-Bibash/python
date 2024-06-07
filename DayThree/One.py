stra='123567890'


print(type(stra[1]))
print("--------------------------------")


for i in range(2,10,2):


    print(type(i))

    print(stra[i])


    print(isinstance(i, int)) ## if i is int return true
     
print("--------------------------------")


list = [1, '2', "biabsh", '3', '123567890',0]

for i in range(len(list)):

     print(type(i))

     if isinstance(list[i], str):

         continue
     print(list[i])
          
          
          


