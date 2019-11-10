# https://www.codewars.com/kata/take-a-ten-minute-walk/train/python/5dc08c5f576239001ea5cec5

def isValidWalk(walk):
    #determine if walk is valid
    print(walk)
    if len(walk) != 10:
        return False
    
    horizonal_count = 0
    vertical_count = 0
    for elem in walk:
        if elem == "n":
            vertical_count += 1
        elif elem == "s":
            vertical_count -= 1
        elif elem == "w":
            horizonal_count += 1
        else:
            horizonal_count -= 1
    if horizonal_count == 0 and vertical_count == 0:
        return True
    return False
