mylist=["1","4","3","4","5","6","7","8","2"]
temp=mylist[-1]
temp2=mylist[0]
mylist[0]=temp
mylist[-1]=temp2
print(mylist)