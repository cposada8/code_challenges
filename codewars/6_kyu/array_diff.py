# https://www.codewars.com/kata/array-dot-diff/train/python/5dbca771f1e68a0017a8f60c


def array_diff(a, b):
    for elem in b:
        a = [x for x in a if x != elem]
    return a
