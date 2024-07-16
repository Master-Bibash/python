def lastChar(word):
    return word[-1]


print(lastChar("word"))


def findthedigit(digit):
    word = "bibash"
    if (word.__contains__(digit)):
        return True
    else:
        return False


print(findthedigit("1"))

# eight


def getPalindrome(sent):
    word = ''
    for i in range(len(sent)-1, -1, -1):
        word = word + sent[i]
    return word


def isPalindrome(word):
    word = word.lower()
    return getPalindrome(word) == word


# nine
def isthereS(word):
    if (word.lower().__contains__("u")):
        return True
    else:
        return False


print(isthereS("worUd"))
# ten


def listEven(numbers):
    a = []
    for i in numbers:
        if (i % 2 == 0):
            a.append(i)
    print(a)


listEven([1, 2, 3, 4])

# elevan


def findMax(numbers):
    if not numbers:
        print("List is empty")
        return

    max_val = numbers[0]
    for i in numbers:
        if i > max_val:
            max_val = i
    print(max_val)


findMax([1, 2, 3, 4])

# elevan


def findVowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in words:
        if char in vowels:
            return True
    return False


print(findVowels("pp"))


def findConso(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for char in words.lower():
        if char.isalpha() and char not in vowels:
            count += 1

    if count > 0:
        print("There are consonants")
    else:
        print("No consonants")


findConso("words")
