'''Imagine you are given two sorted lists of integers, 
list1 and list2. Your task is to write a Python function 
that will return a new sorted list that comprises elements 
from list1 and list2, but without any common elements in both lists. 
This new list must also be sorted in ascending order.

For instance, if you are given list1 = [2, 5, 7, 10] and 
list2 = [1, 5, 9], your function remove_common_elements([2, 5, 7, 10], [1, 5, 9]) 
should return [1, 2, 7, 9, 10] because 5 is a common element in both 
lists and should be removed.
'''

def remove_common_elements(list1, list2):
    # TODO: Implement the function here
    res = []
    if list1 == list2:
        return res
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            # print(list1[i],list2[j])
            res.append(list1[i])
            i += 1
            if i == len(list1) or j == len(list2):
                break
        if list1[i] < list2[j]:
            # print(list1[i],list2[j])
            res.append(list2[j])
            j += 1
            if i == len(list1) or j == len(list2):
                break
        if list1[i] == list2[j]:
            i += 1
            j += 1
            if i == len(list1) or j == len(list2):
                break
    while i < len(list1):
        # print(i, j)
        if list1[i] not in res:
            res.append(list1[i])
            i += 1
    while j < len(list2):
        # print(j)
        if list2[j] not in res:
            res.append(list2[j])
            j += 1
    print(res)
remove_common_elements([1, 2, 3], [2, 3, 4])