word = "biabsh"

count = 0
for i in word:
    if i in {"a", "e", "i", "o", "u"}:
        count = count+1
print(count)


# lets revers
print(range(len(word)-1, -1,-1))
each = ' '
arr=[]
for i in range(len(word)-1, -1,-1):
     each=each+word[i]
print(f"reverse is {each}")
     



# takes list and sum
# numbers=[]
# total = 0
# for i in range(5):
#      val=input("enter number")
#      numbers.append(int(val))
#      total += numbers[i]
# print(f"total is {total}")



#taks the longest string
word1="raju"
word2="pappu"
word3="baburam"

longest_word =word1

if len(word2)>len(longest_word):
     longest_word=word2
if len(word3) > len(longest_word):
     longest_word=word3

print(f"longest word is {longest_word} with length {len(longest_word)}")

print("-------------------------------- --------------------------------")

# Write a Python program that prints all the numbers from 1 to 20 that are divisible by 3.

isdivisible=[]

for number in range(1,20,1):
     if number%3==0:
          isdivisible.append(number)
print(isdivisible)


print("-------------------------------- --------------------------------")
# Write a Python program that takes a list of numbers and returns a new list with only the even numbers.

def giveeven(items):
     items=[num for num in items if num%2==0]
     return items;
print(giveeven([1,2,3,4,5,6]))

print("-------------------    -------------------------------")

## Write a Python program that takes a string and returns a new string with all the vowels removed.

def giveWordsWithoutVowels(name):
     newname = ""
     for char in name:
          if char in {"a","e","i","o","u"}:
               continue
          newname+=char
     return newname

print(giveWordsWithoutVowels("bibash"))
          




          