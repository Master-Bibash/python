listData = ["apple", "orange", "apple", "orange", "orange"] ##list
arr={"a","a"}
word_count = {
     "a":1,
     "b":2
}
# word_count
# print()
# print(listData.count)
for word in listData:
     if word in listData:
          listData[word] = listData[word]+1
     else:
          listData[word] = 1
print(listData)
