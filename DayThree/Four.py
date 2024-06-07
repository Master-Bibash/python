List=[1,2,3,5,90]
inputuser = int(input("Enter a number to add\n"))
List.append(inputuser)

user = int(input("Enter a number\n"))
print("--------------------------------")
for i in range(len(List)):
     if user is List[i]:
          print(f"found in index {i}")
          break
print("-------------With Funtion-------------------")

def search(array,value):
     for i in range(len(array)):
          if(array[i]==value):
               return i


print(search(List, user))
          

     
print("--------------------------------")
names='apple,cat,ball,fast,s,tatt'
names_list=names.split(',')
# print(names_list)

for i in range(len(names_list)):
          print(names_list[i])