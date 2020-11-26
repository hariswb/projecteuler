# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers 
# and the square of the sum is 3025−385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.
#
# Just Brute Force :|
# I tried 10^6 natural numbers and it started to slow. I tried with 10^10
# and my wooden laptop frozen :\

import math
import functools
def sumSquareDifference(n):
    sumOfTheSquares = sum([x**2 for x in range(1,n+1)])
    squareOfTheSum = functools.reduce(lambda i,j: i+j, [x for x in range(1, n+1)])**2
    return squareOfTheSum - sumOfTheSquares
sumSquareDifference(100)
