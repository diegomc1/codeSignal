'''You are given an array of integers, 
and your task is to sort the array using the 
Selection Sort method, wherein the smallest 
integer is selected from the array and swapped 
with the first position. This process is repeated 
until the array is sorted.

For example, given an array [3, 1, 2, 4, 5], 
your function should return [1, 2, 3, 4, 5].

The expected time complexity is O(n 2).'''

def selection_sort(arr):
    # TODO: Implement selection sort algorithm
    # dum = 0
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if arr[i] < arr[j]:
    #             dum = arr[j]
    #             arr[j] = arr[i]
    #             arr[i] = dum
    # return(arr)

    for i in range(len(arr)):
        mini = i 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        (arr[i], arr[mini]) = (arr[mini], arr[i])
    print (arr)
        
selection_sort([3, 1, 2, 4, 5])