# https://www.codewars.com/kata/valid-braces/train/python/5dbcb22f9c7058001a3d4ff5


def validBraces(string):
    openers = "({["
    closers = ")}]"

    stack = []
    for let in string:
        if let in openers:
            stack.append(let)
        else:  # it's a closer character
            if len(stack) == 0:  # you cannot pop an element
                return False

            actual_opener = stack.pop()
            # compare if the opener is the same type as the closer
            if openers.index(actual_opener) != closers.index(let):
                return False
    return len(stack) == 0
