def find_first_vowel(word):
    for char in word:
        if char in 'aeiouAEIOU':
            return char
    return None


def find_first_consonant(word):
    vowels = 'aeiouAEIOU'
    for char in word:
        if char.isalpha() and char not in vowels:
            return char
    return None


def countvowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


def countConsonants(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char.isalpha() and char not in vowels:
            count += 1
    return count


def evennumbersupto(limit):
    evens = []
    num = 0
    while num <= limit:
        if num % 2 == 0:
            evens.append(num)
        num += 1
    return evens


def evenandoddnumbersupto(limit):
    evens = []
    odds = []
    num = 0
    while num <= limit:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
        num += 1
    return evens, odds
