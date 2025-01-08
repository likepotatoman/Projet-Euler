import numpy as np
def factors(n):
    factors = []
    for i in range(1,round(np.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if round(n / i) != i:
                factors.append(round(n / i))
    factors.sort()
    return factors

total = 0
for i in range(1,10000):
    sum_of_proper_divisors = sum(factors(i)) - i
    amicable_pair = sum(factors(sum_of_proper_divisors)) - sum_of_proper_divisors
    if  i == amicable_pair and i != sum_of_proper_divisors:
        print(sum_of_proper_divisors, i)
        total += i
print(total)
