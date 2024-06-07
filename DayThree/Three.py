# file_path = 'D:/python/DayThree/requirement.txt'

# file = open("D:\python\python_files_in_loop\my_file.txt", "x")
# f.write("biabsh")

for i in range(1, 51):
    filename = f"text{i}.txt"
    with open(filename, "w") as file:
        file.write(f"this{filename}\n")
