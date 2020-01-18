def productTriplet():
    result = 1
    for a in range(1,1000):
        for b in range(a,1000):
            c = 1000 - a - b
            if c > b and a+b+c == 1000:  
                if a**2 + b**2 == c**2: 
                    result = a*b*c
        if result > 1:
            break                
    return result
productTriplet()