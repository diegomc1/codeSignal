'''You are given an integer number, 1≤n≤10^6
 . Your task is to write a function next_prime(n), 
 that takes an integer n as input and returns the smallest 
 prime number larger than n.

Here are some examples:

next_prime(7) should return 11, because 11 is the next prime number after 7.
next_prime(13) should return 17, because 17 is the next prime number after 13.
next_prime(50) should return 53, because 53 is the next prime number after 50.'''


def is_prime(n):
    if n < 2:
        return False
    # if a number doesnt have divisors between 2 and n**0.5 (sqrt) is prime
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: # If n is divisible by i, it's not prime
            return False
    return True

def next_prime(n):
    # TODO: implement the function to find the next prime number after n
    sec_prime = n + 1
    while True:
        prime = is_prime(sec_prime)
        if prime == False:
            sec_prime += 1
        else:
            break
    return sec_prime
test = next_prime(7)
print(test)



              