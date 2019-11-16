# https://www.codewars.com/kata/replace-with-alphabet-position/train/python/5dbc94054ca997002a4ec78d


def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    positions = []

    for let in text:
        if let.lower() in alphabet:
            positions.append(str(alphabet.find(let.lower()) + 1))

    return " ".join(positions)
