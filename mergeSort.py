def merge_sort(arr):
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]  # Left half of the array
    right_half = arr[mid:]  # Right half of the array
    # Recursively sort both halves
    # print(left_half, right_half)
    left_half = merge_sort(left_half)
    # print('left ',left_half)
    right_half = merge_sort(right_half)
    # print('right ', right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []  # Initialize an empty list to store the merged result
    i = j = 0  # Initialize pointers for the left and right halves
    # print(left, right)

    # Merge the two halves by comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left half
    while i < len(left):
        result.append(left[i])
        i += 1

    # Append any remaining elements from the right half
    while j < len(right):
        result.append(right[j])
        j += 1
    # print(result)
    return result


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)