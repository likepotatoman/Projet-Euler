def is_prime(n):
    if n == 1:
        return False
    for i in range(2,round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(n, found_primes = {1 : 2}):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2,round(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for i in range(n, 0, -1):
        if i in found_primes:
            last_prime_index = i
            last_calculated_prime_value = found_primes[i]
            break
        
    for i in range(n - last_prime_index):
        last_calculated_prime_value += 1
        while is_prime(last_calculated_prime_value) == False:
            last_calculated_prime_value += 1
        found_primes[last_prime_index + i + 1] = last_calculated_prime_value
    return found_primes[n]


i = 1
while True :
    flag = False
    j = 1
    while (tested_prime := prime(j)) < i:
        k = 0
        while tested_prime + 2 * k**2 < i:
            k += 1
        if tested_prime + 2 * k**2 == i:
            flag = True
        j += 1
    if flag == False and not (is_prime(i)) :
        print(i)
        exit()
    i += 2
