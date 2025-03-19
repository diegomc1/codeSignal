'''You are given a list of integers. Your task is to write a Python function
 to find the second-largest number among these integers. If the list has fewer
   than two unique numbers, return None.

You are not allowed to use any built-in Python functions or methods such as 
sorted(), max(), or sort(). Instead, you should implement the task using 
basic list operations.'''

from typing import List, Optional

def second_max(nums: List[int]) -> Optional[int]:
    # TODO: Find the second largest number in 
    if not nums or len(nums) == 1:
        return None
    # Initialize the largest and second-largest variables
    max_num = float('-inf')
    sec_max = float('-inf')
    for x in nums:
        if x > max_num:
            # Update second_largest to the current largest
            sec_max = max_num
            # Update largest to the current number
            max_num = x
        elif x > sec_max and x != max_num:
            # Update second_largest if the number is greater than it but not equal to largest
            sec_max = x
    # If second_largest is still -inf, it means there are fewer than two unique numbers
    if sec_max == float('-inf'):
        return None
second_max([10, 10, 10, 10])