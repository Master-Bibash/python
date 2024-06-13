fileurl="D:\python\Day_Seven\input.txt"

with open(fileurl,'r') as f:
     for line in f.readlines():
          array=line.strip().split()
          student_scores={}
          name=array[0]
          print(name)
          scores=[]
          for score in array[1:]:
               scores.append(int(score))
               total_score=sum(scores)
               num_score=len(scores)
               avg_score=total_score/num_score
               student_scores[name]=avg_score
          print(student_scores)
          # # print(student_scores)
          # with open(fileurl, 'w') as file:
          #      for name, avg_score in student_scores.items():
          #           print(name, avg_score)

