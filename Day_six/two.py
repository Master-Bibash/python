word_count={}
word_arr=[]
with open("Day_six/file.txt", 'r') as f:
     for line in f.readlines():
          word_arr+=line.split(',')

     print(f"the word count is {word_arr.__len__()} and item is {word_arr}")
