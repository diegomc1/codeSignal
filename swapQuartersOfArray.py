'''You are given an array of n integers. Write a function that rearranges 
the array so that the middle half of the elements (considering the left 
and right quarters have been eliminated) move to the beginning of the array. 
The remaining elements, the left and right quarters, should move to the 
end of the array. If n is not divisible by 4, include the extra elements 
in the middle half.

Specifically:

Divide the array into four quarters.
Move the second and third quarters to the front.
Move the first and fourth quarters to the back.
The function should modify the array in place.

For example, if the input array is [1, 2, 3, 4, 5, 6, 7, 8], your function 
should rearrange the array to [3, 4, 5, 6, 1, 2, 7, 8].

The solution should have a time complexity of O(n).'''
def rearrange_array(arr): 
    n = len(arr) 
    if n < 4: 
        return 0
# Calculate quarter sizes
    quarter = n // 4
    middle_start = quarter
    middle_end = n - quarter

    # Create new indices to hold the rearranged parts
    middle_half = arr[middle_start:middle_end]
    print(middle_half)
    left_quarter = arr[:middle_start]
    print(left_quarter)
    right_quarter = arr[middle_end:]
    print(right_quarter)

    # Rearrange in-place
    arr[:] = middle_half + left_quarter + right_quarter
# Example usage
arr = [-9, -7, -5, -3, -1, 0, 1, 3, 5, 7, 9]
rearrange_array(arr)
print(arr)  # Output: [-5, -3, -1, 0, 1, 3, 5, -9, -7, 7, 9]
