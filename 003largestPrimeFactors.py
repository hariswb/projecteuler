# Problem: The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# 
# The algorithm only works with squarefree composite number in which no prime factor repeats itself like 42 = 2 * 3 * 7, such as the one the question asks 

def largestPrimeFactor(num):
    ## dividing the number until it's quotient is 1 
    quotient = num
    i = 1
    while quotient > 1:
        i += 1
        if quotient % i == 0:
            quotient/=i
            print(i, quotient)
    return(i)
largestPrimeFactor(600851475143)
