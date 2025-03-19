'''You work with large data sets in Python, and typically, 
the data arrive sorted within individual batches but not 
across all batches. You are given n lists, where each list 
is sorted in ascending order. The function should return a 
single list consisting of all elements from all lists, 
sorted in ascending order.

The time complexity of your solution should be O(n⋅m), 
where n is the total number of lists and m is the maximum 
length of any list.

Your solution is not allowed to use built-in functions like 
sorted, sort, or additional libraries like heapq.'''

def merge_n_sorted_lists(arr: list[list[int]]) -> list[int]:
    # TODO: implement the function to merge sorted lists
    pointers = [0] * len(arr)
    res = []
    while True:
        min_val = None
        # Set the pointers helpers index
        index = -1
        for i in range(len(arr)):
            # Compares value of pointer must be less than the number of columns
            if pointers[i] < len(arr[i]):
                # set current value to the ith row and the pointers column
                current_value = arr[i][pointers[i]]
                if min_val is None or current_value < min_val:
                    min_val = current_value
                    index = i

        # If no more elements are left to process, break the loop
        if min_val is None:
            break

        # Append the smallest element to the result
        res.append(min_val)
        # Move the corresponding pointer forward
        pointers[index] += 1 
    print(res)
arr = [-5], [-4], [-3], [-2], [-1]
merge_n_sorted_lists(arr)