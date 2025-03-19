'''You need to implement the Insertion Sort algorithm. 
Given a list of n integers, the algorithm must sort the 
elements of this list in increasing order using Insertion Sort.

The Insertion Sort algorithm iterates over an index from 
left to right. As the index moves to the right, it "inserts" 
the element at the index into the correct location in the 
"already sorted" portion of the list on the left.'''

def insertion_sort(arr):
    # TODO: implement the Insertion Sort algorithm
    n = len(arr)
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key
    return(arr)

print(insertion_sort([5, 2, 4, 6, 1, 3]))