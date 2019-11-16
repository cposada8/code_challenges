# https://www.codewars.com/kata/catching-car-mileage-numbers/train/python/5dc46b4606d013000fabb31c


def followed_by_all_zeroes(number):
    return int(number[1:]) == 0


def all_digits_the_same(number):
    return len(set(number)) == 1


def incr_or_decr(number):
    return number in "1234567890 9876543210"


def is_palindrome(number):
    return number == number[::-1]


def validate_number(number, awesome_phrases):
    # this function return True if a number is interesting
    strnum = str(number)
    if number > 99:
        if followed_by_all_zeroes(strnum) \
                or all_digits_the_same(strnum)\
                or incr_or_decr(strnum)\
                or is_palindrome(strnum)\
                or number in awesome_phrases:
            return True
    return False


def is_interesting(number, awesome_phrases):

    if validate_number(number, awesome_phrases):
        return 2
    if validate_number(number+1, awesome_phrases):
        return 1
    if validate_number(number+2, awesome_phrases):
        return 1

    return 0
