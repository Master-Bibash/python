def findOddorEven(num):
    if (num % 2 == 0):
        return True
    else:
        return False


print(findOddorEven(7))

# second
name = "bibash"


def findreverse(word):
    reverse = ''
    for i in range(len(word)-1, -1, -1):
        reverse = reverse + word[i]
    return reverse


print(findreverse("raj"))
