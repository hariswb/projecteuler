import math
import time

def eratosthenes(integer):
    """
    Takes an integer
    find all the prime below that integer
    uses the old sieve of eratosthenes
    with python set for faster performance
    
    For searching all primes under 2 million, 
    this takes around 1 second
    """
    start=time.time()
    p = set(range(2,integer+1))
    i = 2
    while i < integer:
        if i in p:
            p -= set(range(i*2,integer+1,i))
        i+=1
    print("time spent: ", round(time.time()-start,3), "Seconds")
    return sum(p)
print(eratosthenes(2000000))
