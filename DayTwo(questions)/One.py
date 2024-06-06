from cmath import inf

number=[1,2,3,8,90,50,6];

# for i in number:
#      print(i);

# # finding the max element

# length =len(number);
# largest_element=float(-inf)
# for i in range(length):
#      element=number[i]
#      if element> largest_element:
#           largest_element=element
# print(largest_element);

# num1=input('enter number1')
# num2=input('enter number2')
# print(num1)
# print(num2)

print("-------------------------------")
# sum_arry=[]
# total=0;
# for i in range(10):
#      num=input("enter num")
#      sum_arry.append(num)
#      total+=int(sum_arry[i])

# print("total is ",total)

# #print the reverse using while loop
# print("enter a word\n")
# word="apple"
# length_word=len(word)
# i=0 
# rev_word=''
# while length_word > i:
#      if (len(rev_word)!=len(length_word)):
#           rev_word+=word[length_word]
#           length_word=length_word-1;



# a=[1,2,3,4,5,6,7,8,9,9]
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

list1=["m","na","i","Ke"]
list2=["y","me","s","lly"]

# for i,j in zip(lis1,list2):
#      print(i+j)

for i in range(len(list1)):
   final_value= list1[i] + list2[i]
   if "name" in final_value:
     list1[i] += list2[i]
   
print(list1)

word="ball"
new_word=""
print(range(len(word)))
for i in range(len(word)):
    print(i)


print(new_word)