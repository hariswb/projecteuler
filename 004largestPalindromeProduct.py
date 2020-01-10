# Problem: A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def checkPal(num):

    arr = []
    i = 1
    while num > 0:
        arr.append(round((num/10 - num//10)*10))
        num //= 10
        i += 1
    newArr = [x for x in arr]
    newArr.reverse()
    if arr == newArr:
        return True
    else:
        return False

x = 0
y = 0
for i in range(999*999, 100*100, -1):
    if checkPal(i) == True:
        for j in range(999,100,-1):
            if i % j == 0 and i/j/100 < 10 and j/100 < 10 :
                x = j
                y = i/j
                print(i, x, y, x/100, y/100)
                break
    if x > 0 and y> 0:
        break

print("It's",x*y, "which is", x,"*",y)