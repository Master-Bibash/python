studentName = {
    'binod': 90,
    'pinky': 25,
    'lalu': 75,
    'yadav': 25,
}

name = input('what is your name ').lower()

if name in studentName:
    print(f'{name.capitalize()} your marks is {studentName[name]}')
    if studentName[name] >= 80:
        print('You have distinction')
    elif studentName[name] >= 60:
        print('You have second division')
    elif studentName[name] >= 40:
        print('You secured third division')
    else:
        print(f"Mom is giving chapal received at {studentName[name]}km/hr ")


else:
    print(f'{name.capitalize()} not found')
