'''You are given an array of n integers. Your task is to return the number 
of unique elements in the array — an element is unique if it appears only 
once in the array. You cannot use any built-in Python functions to achieve this.

For example, count_unique_elements([1, 2, 3, 2, 4]) = 3, as there are four 
unique elements in the list - 1, 3, and 4.'''

def get_ocurrences(ocu):
    count = 0
    for i in ocu.values():
        if i == 1:
            count += 1
    return (count)

def count_unique_elements(lst):
    # TODO: Implement the function that counts unique elements in the given list.
    a = {}
    count = 1
    for i in lst:
        if i not in a.keys():
            a[i] = count
        else:
            a[i] = count + 1
    ocu = get_ocurrences(a)
    return (ocu)

count_unique_elements([1, 1])