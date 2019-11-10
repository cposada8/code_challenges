# https://www.codewars.com/kata/equal-sides-of-an-array/train/python/5dc0937a62dfa40029a2e63d

def find_even_index(arr):
    #your code here
    ans = -1
    # adding the element at possition i in both left and right
    # will make the code easier
    for i in range(len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i+1:])
        if left == right:
            ans = i
            break
    return ans