file_path = 'D:/python/DayThree/requirement.txt'
with open(file_path,'r') as f:
     print("type is",type(f))
     for i in f.readlines():
          print(i)

with open(file_path,"w") as f:
     for i in range(10):
          f.write("hello\n")
     f.close()


