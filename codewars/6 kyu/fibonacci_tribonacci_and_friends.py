# https://www.codewars.com/kata/fibonacci-tribonacci-and-friends/train/python/5dbca63eae5538002975392b

def Xbonacci(signature,n):
    #your code here
    l_s = len(signature)    #the length of signature
    if n <= l_s: # must always be 3
        return signature[:n]
    
    for _ in range(l_s, n):
        actual = sum(signature[-l_s:])
        signature.append(actual)
    return signature