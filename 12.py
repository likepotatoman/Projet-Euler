import numpy as np
def factors(n):
    factors = []
    for i in range(1,round(np.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n / i)
    return factors

print(factors())

triangle_index = 1
while True:
    if len(factors(sum([i for i in range(triangle_index)]))) >= 500:
        print(sum([i for i in range(triangle_index)]))
        exit()
    triangle_index += 1
