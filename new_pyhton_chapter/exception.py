while True:
    try:
        a = int(input("Enter first num "))
        b = int(input("Enter sec num "))
        print(a/b)
    except ValueError:
        print("input must be a number")
