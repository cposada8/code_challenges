# https://www.codewars.com/kata/range-extraction/train/python/5dc86f901178cd0032f05493


def solution(args):
    # your code here
    solutions = []
    i = 0
    last_added = 0
    while i < len(args):
        consecutives = []
        actual_num = args[i]
        consecutives.append(actual_num)
        last_added = i
        for j in range(i+1, len(args)):
            j_num = args[j]
            if j_num-actual_num == 1:
                consecutives.append(j_num)
                actual_num = j_num
                last_added = j
            else:
                break

        if len(consecutives) > 2:
            actual_solution = \
                str(consecutives[0]) + "-" + str(consecutives[-1])
            solutions.append(actual_solution)
        elif len(consecutives) == 2:
            solutions.append(consecutives[0])
            solutions.append(consecutives[1])
        else:
            solutions.append(consecutives[0])
        i = last_added+1

    solutions = ",".join([str(sol) for sol in solutions])
    return solutions
