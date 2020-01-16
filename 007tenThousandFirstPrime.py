import numpy as np

def nthPrime(n):

    # Find asymptotic bound on the nth prime p(n)
    # from prime number theorem
    #lower = n*(np.log(n)+(np.log(np.log(n))-1))
    upper = n*(np.log(n)+np.log(np.log(n)))
    
    # Sieve, prime-counting function all the way through upper bound    
    arr = [x for x in range(0,int(round(upper)))]
    l = len(arr)
    i = 2
    while i < l:
        if i in arr:  
            for x in arr:      
                if x != i and x % i == 0:
                    arr.remove(x)
        i += 1

    # Get the desired nth prime
    return arr[n]

nthPrime(10)
nthPrime(25)
nthPrime(10001) 