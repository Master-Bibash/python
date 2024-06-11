def  count_frequencies(Liststr):
     dict={}
     for i in Liststr:
          if i in dict:
               dict[i]+=1
          else:
               dict[i]=1
     return dict


words = ["apple", "banana", "apple", "orange", "banana", "apple"]

print(count_frequencies(words))
