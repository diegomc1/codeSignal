'''You are given an integer number n. The task is to determine if this number is a perfect square or not.
 A perfect square is a number that can be expressed as the product of an integer with itself. For example,
   1 = 1 * 1, 4 = 2 * 2, 9 = 3 * 3, and 16 = 4 * 4 are perfect squares, but 2, 3, 5, and 6 are not.

Implement a function is_perfect_square(n) that returns True if the given number n is a perfect square 
and False otherwise.'''

def is_perfect_square(n):
    # TODO: implement the function that checks if a number is a perfect square
    if not n:
        return False
    else:
        sqrt = n ** 0.5 
        return(sqrt.is_integer()) 

is_perfect_square(27)