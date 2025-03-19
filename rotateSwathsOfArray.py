'''
You have been given an array of n integers. 
Your task is to write a function that reverses 
the array in groups of k size, and if the last 
group has fewer than k elements, reverse all of them. 
Return the newly organized array after the 
groups have been reversed.

For example, given the array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
and k = 3, the output should be: [3, 2, 1, 6, 5, 4, 9, 8, 7, 10].
The first three elements are reversed to get [3, 2, 1], the next three become 
[6, 5, 4], the following three are [9, 8, 7], and the final one remains [10] 
as there are fewer than k elements remaining.
'''
def rotate(numbers, start, end):
    while start < end:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1
    return (numbers)

def solution(numbers, k):
    # TODO: implement the solution here
    if not numbers:
        return 0
    if k == 0:
        return numbers
    if k == 1:
        return numbers
    if k >= len(numbers):
        rotate(numbers, 0, len(numbers)-1)
        return numbers
    k = k % len(numbers) # Ensure k is within the bounds of the array length
    start = 0
    end = k
    remainder = len(numbers) % k
    # print(remainder, divisor)
    for _ in range(0, len(numbers)-remainder, k):
        rotate(numbers, start, end - 1)
        start = end
        end += k
    rotate(numbers, len(numbers)-remainder, len(numbers)-1)
    print (numbers)

numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution(numbers, k)