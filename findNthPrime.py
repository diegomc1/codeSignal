'''You are given a number n. Your task is to write a function that will 
return the n-th prime number. The expected complexity is 

For example, if n is 1, the function should return 2. If n is 3, 
the function should return the third prime number, which is 5.
'''
def is_prime(n):
    if n < 2:
        return False
    # if a number doesnt have divisors between 2 and n**0.5 (sqrt) is prime
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: # If n is divisible by i, it's not prime
            return False
    return True

def nth_prime(n: int) -> int:
    # TODO: implement the function
    last_item = n - 1
    i = 2
    primes = []
    while n != 0:
        true_prime = is_prime(i)
        if true_prime:
            primes.append(i)
            n -= 1
        i += 1
    print(primes[last_item])

nth_prime(10)