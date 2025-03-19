'''You are provided with two integers, a and b. Your task is to write 
a Python function that checks whether both a and b are co-prime or not.
 Two numbers are said to be co-prime or mutually prime if the only 
 positive integer that divides both of them is 1. 
 The expected complexity is 

print(are_coprime(15, 28))   # Output: True
print(are_coprime(12, 18))   # Output: False

In the first example, the only positive integer that divides both 15 and 28 
is 1; hence, they are co-prime. However, in the second example,
 12 and 18 are divisible by 2 and 3; thus, they are not co-prime.
'''

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
    return prime_factors

def are_coprime(a, b):
    # TODO: implement
    afactors = get_prime_factors(a)
    bfactors = get_prime_factors(b)
    compare = set(afactors).intersection(bfactors)
    if not compare:
        return True
    else:
        return False

print(are_coprime(15, 28))