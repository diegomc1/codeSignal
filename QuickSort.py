def quicksort(arr):
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (here, we choose the last element)
    pivot = arr[-1]

    # Partition the array into two subarrays
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    # Recursively sort the subarrays and combine them with the pivot
    return quicksort(left) + [pivot] + quicksort(right)


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)