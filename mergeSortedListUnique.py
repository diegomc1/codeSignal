'''You are given two sorted lists, each containing n integers. 
Your task is to merge these two lists into a new list such that:

The resulting list is sorted in descending order.
If there are duplicate elements in the two lists, they should 
be merged so that each duplicate appears only once in the final list.
For instance, if you are given two lists, [1, 2, 3, 4, 5] and 
[3, 4, 5, 6, 7], your function should return 
[7, 6, 5, 4, 3, 2, 1] as the merged list.
'''

def merge_sorted_lists_descending_unique(l1, l2):
    # TODO: Implement the function
    if not l1 or not l2:
        return 0
    res = []
    uniqueRes = []
    starti = len(l1) - 1
    startj = len(l2) - 1
    while starti > -1 and startj > -1:
        if l1[starti] >= l2[startj]:
            res.append(l1[starti])
            starti -= 1
        else:
            res.append(l2[startj])
            startj -= 1
    while starti > -1:
        res.append(l1[starti])
        starti -= 1
    while startj > -1:
        res.append(l2[startj])
        startj -= 1
    for num in res:
        if num not in uniqueRes:
            uniqueRes.append(num)
    print(uniqueRes)

    # print(res)
merge_sorted_lists_descending_unique([-10, -9, -8, -7, -6], [-5, -4, -3, -2, -1])