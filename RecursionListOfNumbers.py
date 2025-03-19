'''The task is to write a recursive function solution(n)
 that takes an integer n as an input and returns a list of
   integers from n to 1, inclusive, in decreasing order. 
   Make sure to use recursion in this task.

For example, for n = 5, the output should be [5, 4, 3, 2, 1].'''

list = []
def solution(n):
    # TODO: implement
    if n > 0:
        list.append(n)
        solution(n - 1)
        return list
    return list

print(solution(13))