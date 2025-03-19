'''Your task is to create a Python function called get_prime_factors(n) 
that will return all unique prime factors of an integer n in a list. 
A prime factor of n is a prime number that divides n without leaving a remainder. 
The expected complexity is O(sqrtN)

Note that returned prime factors should be unique and sorted in ascending order
in the resulting list.'''

def get_prime_factors(n):
    """Returns a list of unique prime factors of n in ascending order."""
    prime_factors = set()  # Use a set to store unique prime factors

    # Handle divisibility by 2 separately
    while n % 2 == 0:
        prime_factors.add(2)
        n //= 2

    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            prime_factors.add(i)
            n //= i

    # If n is still greater than 1, it is a prime factor
    if n > 1:
        prime_factors.add(n)

    # Convert the set to a sorted list
    print (sorted(prime_factors))

get_prime_factors(987654)