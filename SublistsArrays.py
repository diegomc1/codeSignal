'''You are provided with two lists of integers, listA and listB. Your task is to determine
 if listB is a contiguous sublist of listA. You need to return True if listB is a contiguous
   sublist of listA, and False otherwise.

A sublist is defined as a subset of consecutive elements within a list. 
For instance, [2, 3] is a sublist of [1, 2, 3, 4] but not a sublist of [1, 3, 2, 4].

Note that you are not allowed to use any built-in Python functions for this task
 except for the len() function to get the length of a list. All other operations 
 should be executed with basic Python programming constructs.'''

def solution(listA, listB):
    # TODO: implement solution
    lena = len(listA)
    lenb = len(listB)

    # Edge cases
    if lenb == 0:
        return True  # An empty list is always a sublist
    if lena == 0 or lenb > lena:
        return False  # listB cannot be a sublist of listA
    
    # Iterate through listA
    for i in range(lena - lenb + 1):
        match = True
        # Check if the next lenB elements match listB
        for j in range(lenb):
            if listA[i + j] != listB[j]:
                match = False
                break
        if match:
            return True   
    return False 

print(solution([1, 2, 3, 4],[3, 4]))