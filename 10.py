import numpy as np
def is_prime(n):
    for i in range(2,round(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


total = 0
prime = 1
while prime < 2000000:
    prime += 1
    while is_prime(prime) == False:
        prime += 1
    total += prime
print(total - prime)
