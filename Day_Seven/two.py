scores = {}
with open("D:\\python\\Day_Seven\\runner.txt", 'r') as f:
    scores = {}
    for line in f.readlines():
        data = line.strip().split()
        name = data[0]
        persons = []
        for person in data[1:]:
            persons.append(int(person))
            total_score = sum(persons)
        # print(total_score)
        scores[name] = total_score
    short_run = min(scores.values())
    print(short_run)

with open("D:\\python\\Day_Seven\\runner.txt", 'a') as file:
    for name, score in scores.items():
        file.write(f"name is {name} and run is {score}\n")
