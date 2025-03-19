'''You are provided with two input lists that contain n and m integers, 
respectively. Both lists are sorted in non-decreasing order — i.e., 
every element is either equal to or larger than the preceding one.

Your task is to return a new list that results from merging the two 
input lists so that the final output list is also in non-decreasing order. 
It should contain all the elements of the two lists, 
maintaining their order within the lists.

Your solution should not use the built-in sort function of Python 
but should instead use a technique similar to the one used in the 
lesson. The expected time complexity is O(n+m).

For instance, if the two input lists are [1, 3, 5, 7, 9] and 
[2, 2, 3, 4, 6, 6], your function should return 
[1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 9].
'''

def solution(l1, l2):
    # TODO: implement the function to merge two lists and return merged list
    res = []
    starti = 0
    startj = 0
    while starti < len(l1) and startj < len(l2):
        print(starti, startj)
        if l1[starti] <= l2[startj]:
            res.append(l1[starti])
            starti += 1
        else:
            res.append(l2[startj])
            startj += 1
    while starti < len(l1):
        res.append(l1[starti])
        starti += 1
    while startj < len(l2):
        res.append(l2[startj])
        startj += 1
    print(res)
solution([1, 3, 5, 7, 9], [2, 2, 3, 4, 6, 6])