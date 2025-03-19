'''You are given a list of n integers. The goal of this task 
is to return the reversed list of integers without using any
 built-in Python functions or methods related to 
 reversing a list.'''

def solution(numbers):
    # TODO: Implement the function that reverses a list of numbers.
    rev = []
    for i, val in enumerate(numbers):
        rev.append(numbers[-(i+1)])
    return rev
print(solution([5, 4, 3, 2, 1]))