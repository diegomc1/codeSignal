'''You are given an array of n integers. 
Your task is to reverse the array without using 
any additional lists or the built-in reversed() function.

Amend the array in-place and return the array. 
In-place here means you are not allowed to use any 
additional lists in your solution.'''

def solution(arr):
    # TODO: Implement in-place array reverse.
    prev = 0
    dum = 0
    for i in range(-1, (-len(arr) -1)//2, -1):
        dum = arr[prev]
        arr[prev] = arr[i]
        arr[i] = dum
        prev +=  1
    return (arr)
arr = [7, 2, 6, 3, 8, 9, 1]
solution(arr)
