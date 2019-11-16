# https://www.codewars.com/kata/weight-for-weight/train/python/5dc337ddf0be08003201fe50


def sum_digits(number):
    suma = 0
    for digit in number:
        suma += int(digit)
    return suma


def order_weight(strng):
    # your code
    numbers = strng.split()
    num_sum = []
    sums = []
    for num in numbers:
        s_d = sum_digits(num)
        num_sum.append([num, s_d])
        sums.append(s_d)

    sums = list(set(sums))  # getting the unique elements
    sums.sort()

    # choosing the elements
    results = []
    for actual_sum in sums:
        # select all the elements where the sum digit is equal to sum_digit
        elems = [x for x, y in num_sum if y == actual_sum]
        elems.sort()
        results += elems

    return " ".join(results)
