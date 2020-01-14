#2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number 
# that is evenly divisible by all of the numbers from 1 to 20?
#
# It seems like this code is overly complicated 
# and the names are confusing lol

def factorize(number):
    num = number
    factors = []
    while num > 1:
        for i in range(2, number+1):
            if num % i == 0:
                num /= i
                factors.append(i)
                break
    return factors
                
def smallestMultiple(n):
    factors = [factorize(x) for x in range(2,n+1)]
    primes = [list(set(x)) for x in factors]
    #print(factors, "\n",primes)
    primePowers = []
    result = 1
    for primes, factors in zip(primes, factors):
        for x in primes:
            #print(primes, factors, [x, factors.count(x)])
            primePowers.append([x, factors.count(x)])
        #print("{} {}".format(primes, factors))
    primePowers.sort(key= lambda tup: tup[0])
    #print(primePowers)
    for i in range(2,n+1):
        uniquePrimes = [x for x in primePowers if x[0] == i]
        uniquePrimes.sort(key= lambda tup: tup[1])
        #print(uniquePrimes)
        if len(uniquePrimes) > 0:
            largestUniquePrime = uniquePrimes[-1]
            #print(largestUniquePrime, largestUniquePrime[0]**largestUniquePrime[1])
            result *= (largestUniquePrime[0]**largestUniquePrime[1])
    return result        

smallestMultiple(10)
smallestMultiple(20)
smallestMultiple(1000)