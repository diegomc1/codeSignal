def find_min(nums):
    # TODO: implement the function to find the minimum number from a list
    max_element = nums[0]
    if not nums:
        return None
    else:
        for vals in nums:
            if max_element > vals:
                max_element = vals
        print(max_element)
        return max_element
            
lst =[1,2,3,4,5,6]
find_min(lst)