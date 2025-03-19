'''You are given a list of n integers and a number k. 
Your task is to shuffle the array in such a way that, starting 
from the first element, every k-th element moves to the 
end of the array.

For instance, if nums = [1, 2, 3, 4, 5, 6, 7, 8] and k = 3, 
the output should be [1, 2, 4, 5, 7, 8, 3, 6]. Here, the 3rd 
element 3 and the 6th element 6 (every 3rd element starting 
from the first) are moved to the end of the array.'''

def shuffle_array(nums, k):
    # TODO: implement the function here
    if k <= 0 or k > len(nums):
        return nums  # Edge case: invalid k
    # Collect every k-th element
    k_elements = []
    write_index = 0
    for i, num in enumerate(nums, start=1):
        if i % k == 0:
            k_elements.append(num)
        else:
            #Moves number to the left
            print(num)
            nums[write_index] = num
            print(write_index)
            write_index += 1
    # Append the k-th elements to the end
    for i, num in enumerate(k_elements):
        nums[write_index + i] = num
    return(nums)

nums = [766, 243, -12, 24, 0, 41]
k = 2  
shuffle_array(nums, k)