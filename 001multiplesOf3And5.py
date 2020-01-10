# Problem: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


import functools
def sumOfMultiples(a,b):
    def multiples(num):
        return [y for y in range(1,1000) if y % num == 0]
    
    a_not_in_b = [x for x in multiples(a) if x not in multiples(b)]
    a_or_b = a_not_in_b + multiples(b)
    return functools.reduce(lambda i,j: i+j, a_or_b)

sumOfMultiples(3,5)