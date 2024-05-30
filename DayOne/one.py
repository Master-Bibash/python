# making an empty disctionary 

file={
     'age':22
};
file.update(
     {
          "name":"bibash",
          'gender':"male",
          "names":{
             "parent":[
                "father",
                "mother"
             ]
               
          }
     }
),

print(file["names"]["parent"]);


# loop examples
number=[1,2,3,4,5,6,7,8];
for num in number:
     print("num is"+str(num),);


i=1;
while i<=6:
     print(i)
     i+=i;     

