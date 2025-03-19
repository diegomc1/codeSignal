''' ROTATE ARRAY '''

def rotate_array(nums, k):
    k = k % len(nums)  # Ensure k is within the bounds of the array length
    rotated = nums[-k:] + nums[:-k]
    return rotated

# Example
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(nums, k))  # Output: [5, 6, 7, 1, 2, 3, 4]