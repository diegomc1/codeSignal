'''You are given an array of integers. Your job is to return the count
 of even and odd integers in the given array without using any built-in 
 Python methods.

Your function should return a tuple in the format (even_count, odd_count),
where even_count represents the number of even integers and odd_count
represents the number of odd integers in the provided array.'''
def solution(nums):
    # TODO: implement the function to return a tuple (even_count, odd_count)
    oddcounter = 0
    evencounter = 0
    counter = 1
    for i, val in enumerate(nums):
        counter += i
        if counter % 2 == 0:
            evencounter += 1
        if counter % 2 != 0:
            oddcounter += 1
    print(evencounter,oddcounter)

nums=[-2]
solution(nums)