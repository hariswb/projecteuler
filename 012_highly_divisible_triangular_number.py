def get_base_factors(num):
    factors = [1,num]
    i = 2
    found_all = False
    while not found_all:
        if num % i == 0:
            divisor =num//i 
            factors.append(i)  
            factors.append(divisor)  
            num = divisor
            i = 2
            if divisor == 1:
                found_all=True
        else:
            i+=1
        
    return sorted(set(factors))


def get_factors(num):
    factors = get_base_factors(num)
    end = False
    current = 0
    i = 0
    new = []
    while not end:
        product = factors[current] * factors[i]        
        if product not in factors and factors[-1] % product == 0:
            new.append(product)

        if factors[-1] == factors[current]:
            end =True

        if factors[-1] == factors[i]:
            factors += new
            factors = sorted(factors)
            new = []
            i = current
            current +=1

        i+=1
    
    return factors
        
found = False
i=1
triangle_number = 1
factors_number = 0
while not found:
    if triangle_number > 1:
        factors_number = len(get_factors(triangle_number))

    print(f'{i}: {triangle_number} ({factors_number})')
    
    if factors_number >= 500:
        found=True

    i += 1
    triangle_number+=i

    








    