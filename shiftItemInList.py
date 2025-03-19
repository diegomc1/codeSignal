'''In this problem, you are given a list of n integers. Additionally, 
you are given an integer shift, which represents the number of 
positions each element in the list should be moved.

Your task is to create a Python function that should shift every
 element in the list to the right (for a positive shift) or to the
   left (for a negative shift) by shift positions. The shift should
 be circular — the last element should be moved to the start of the
 list if shift is positive, and vice versa.

Please implement this without the usage of any built-in functions
 of Python to shift, sort, or move items in the list.
 Your solutions efficiency should be O(n).'''

def circular_shift(arr, shift):
    """Shifts the elements of the list circularly by the given shift."""
    n = len(arr)
    if n == 0:
        return arr  # Edge case: empty list

    # Normalize the shift to handle cases where shift > n or shift < 0
    shift = shift % n  # Ensures shift is within the range [0, n-1]

    # Helper function to reverse a portion of the list
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire list
    reverse(0, n - 1)
    # Step 2: Reverse the first `shift` elements
    reverse(0, shift - 1)
    # Step 3: Reverse the remaining elements
    reverse(shift, n - 1)

    return arr