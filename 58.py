def is_prime(n):
    if n == 1:
        return False
    for i in range(2,round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

total_diagonal = 1
number_of_primes = 0
i = 1
num_to_add = 2

for j in range(4):
    i += num_to_add
    if is_prime(i):
        number_of_primes += 1
    total_diagonal += 1
num_to_add += 2

while number_of_primes / total_diagonal > 0.1:
    for j in range(4):
        i += num_to_add
        if is_prime(i):
            number_of_primes += 1
        total_diagonal += 1
    num_to_add += 2
print(i**0.5)
