import numpy as np
def factors(n):
    factors = {1}
    for i in range(2,round(np.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(int(n / i))
    return factors

total = 0
abundant_numbers = []
for i in range(1,28133):
    if sum(list(factors(i))) > i:
        abundant_numbers.append(i)

abundant_numbers_sums = set()
for i in range(len(abundant_numbers)):
    for j in range(len(abundant_numbers)):
        abundant_numbers_sums.add(abundant_numbers[i] + abundant_numbers[j])

for i in range(28123):
    if i not in abundant_numbers_sums:
        total += i

print(total)
