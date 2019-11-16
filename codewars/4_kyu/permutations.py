# https://www.codewars.com/kata/permutations/train/python/5dc33d072c135e00168b034b


def permutate_word(a, b):
    # len a will always be 1
    permutations = []
    for i in range(len(b)):
        actual = b[0:i] + a + b[i:]
        permutations.append(actual)

    permutations.append(b+a)
    return permutations


def permutate_list(a, b_list):
    permutations = []
    if len(b_list) == 0:
        return [a]
    for b in b_list:
        permutations += permutate_word(a, b)
    return permutations


def permutations(string):
    permutations = []  # list of all possible permutations

    # seleciono la última letra. La permuto con el resto del string.
    # todas esas permutaciones las guardo en permutations
    # luego selecciono la letra anterior y la permuto con todas las
    # permutaciones que hay en permutations
    for i in range(len(string)-1, -1, -1):
        a = string[i]
        permutations += permutate_list(a, permutations)

    # al final escojo solo las permutaciones válidas. Son las que tienen
    # un número de letras igual al string original (no las que tienen menos)
    # y luego quito las repetidas
    valid_permutations = [x for x in permutations if len(x) == len(string)]
    valid_permutations = list(set(valid_permutations))
    return valid_permutations
