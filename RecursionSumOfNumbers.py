'''You are tasked with creating a function get_sum(n) that calculates
 the sum of all the numbers from n to 1 using recursion.

For instance, get_sum(5) should result in 15 (5 + 4 + 3 + 2 + 1 = 15),
 while get_sum(1) should yield 1.'''

def get_sum(n):
    # TODO: implement this function using recursion
    sum = 0
    if n > 0:
        return n + get_sum(n - 1)
    else:
        return sum

print(get_sum(5))