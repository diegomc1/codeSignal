'''You are given a list of n integers. Your task is to find the zero-based index of the first 
occurrence of this specific value in the list. If the provided value isn't
 found in the list at all, return -1 instead.

In this task, you must implement the solution without using any built-in
 functions or methods. Specifically, the use of the Python index() method 
 of a list is not allowed in your solution.
'''

def solution(lst, val):
    # TODO: Implement the function
    for i, values in enumerate(lst):
        if values == val:
            return i
    return -1

print(solution([1, 2, 3, 4, 5], 5))