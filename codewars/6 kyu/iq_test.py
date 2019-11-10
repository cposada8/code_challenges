# https://www.codewars.com/kata/iq-test/train/python/5dc08fd6e93bc5001fef1583

def iq_test(numbers):
    #your code here
    evenness = [int(num) %2 == 0 for num in numbers.split()]
    
    if evenness.count(1) == 1:
        return evenness.index(1)+1
    else:
        return evenness.index(0)+1