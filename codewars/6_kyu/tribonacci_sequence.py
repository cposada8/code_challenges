# https://www.codewars.com/kata/tribonacci-sequence/train/python/5dbca46b8a422400162c3f63

def tribonacci(signature, n):
    #your code here
    len_signature = len(signature)
    if n <= len_signature: # must always be 3
        return signature[:n]
    
    for _ in range(len_signature, n):
        actual = sum(signature[-len_signature:])
        signature.append(actual)
    return signature