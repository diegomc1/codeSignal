'''
You are provided with an array of n integers and a number k. 
Your task is to perform an anti-clockwise rotation (toward the front) 
of the array by k positions. The rotation should be done in place, 
which means you have to directly manipulate the input array without 
creating a new one. Note that k might be bigger than the array length.

For example, if the input array is [1, 2, 3, 4, 5, 6, 7], and k = 3, 
then after the operation, the input array should look like 
[4, 5, 6, 7, 1, 2, 3].
'''

from typing import List

def rotate(nums: List[int], start: int, end: int):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return (nums)

def anti_rotate_array(nums: List[int], k: int) -> None:
    # TODO: Implement anti-clockwise rotation of the array nums by k steps.
    k = k % len(nums) # Ensure k is within the bounds of the array length
    n = len(nums)
    # reverse the entire array
    rotate(nums, 0, n - 1)
    # reverse from 0 to n-k-1 (overflow)
    rotate(nums, 0, n-k-1)
    # reverse from n-k to n - 1 (overflow)
    rotate(nums, n-k, n - 1)

nums = [1, 3, 5, 6, 8, 2, 4, 9]
k = 5
anti_rotate_array(nums, k)