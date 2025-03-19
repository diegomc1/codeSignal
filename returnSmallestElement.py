''' You are given an array of integers. Your task is to write
 a function in Python that returns the number of times the 
 smallest element appears in the array.

Please note that built-in methods such as min() or count() 
should not be used in this task. Your goal is to accomplish this 
task by iterating over the array elements manually. Try to solve 
the task by doing just a single list traversal.'''

def count_min(numbers):
    # TODO: Implement this function to count the smallest integer in the list.
    counter = {}
    if not numbers:
        return 0
    min_num = numbers[0]
    for x in numbers:
        number = str(x)
        if number not in counter.keys():
            counter[number] = 1
        else:
            counter[number] += 1 
        if min_num > x:
            min_num = x 
    return counter[str(min_num)]
numbers=[-3, -1, -1, -3, -5, -2, -3]
print(count_min(numbers))
        

