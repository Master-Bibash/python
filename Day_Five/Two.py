from cmath import inf


grades={
     "AK":98,
     "B":99,
     "c":70,
     "d":9,
     "E":10,
     "f":99
}

def highest(grades):
     if not grades:
          return None
          max_grade=-1
          top_students=[]
for grade in grades.values():
    if grade > max_grade:
     max_grade=grade

for name,grade in grades.items():
     if grade==max_grade:
          top_students.append(name)
          return top_students
                

highest(grades)
