# https://www.codewars.com/kata/vowel-count/train/python/5dbc980a4ca997001c5372d8


def getCount(inputStr):
    num_vowels = 0
    for leter in inputStr:
        if leter in "aeiou":
            num_vowels += 1
    return num_vowels
