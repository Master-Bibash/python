from cmath import inf
number = [0, 1, 30, 3, 4, 50, 6, 7, 8, 9]
# print(number[3-1]);

# finding the max element
# for i in number:
#      if i==max(number):
#           print(i);


array_length = len(number)
largest_element = float(-inf)
for i in range(array_length):
    element = number[i]
    if element > largest_element:
        largest_element = element
print(largest_element)
