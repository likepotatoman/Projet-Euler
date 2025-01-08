#checks if n is prime
import numpy as np
def is_prime(n):
    for i in range(2,round(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#gives n-th prime
def prime(n):
    prime = 0
    for i in range(n):
        prime += 1
        while is_prime(prime) == False:
            prime += 1
    return prime

#gives prime factors of n
def prime_factors(n):
    prime_factors = []
    prime_index = 2
    while n > 1 :
        while n % prime(prime_index) == 0:
            n = n / prime(prime_index)
            prime_factors.append(prime(prime_index))
        prime_index += 1
    return prime_factors

#gives the factors of n
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

#checks if n is a palindrome
def is_palindrome(n):
    n = str(n)
    n_reverse = str(n)
    n_reverse.reverse()
    if n == n_reverse :
        return True
    return False

#takes a file input and gives a list of lists of integers
from google.colab import files
uploaded = files.upload()
with open("#    #_euler.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()

input = []
for i in range(len(lines)):
    line = lines[i].split(" ")
    input.append(line)

for i in range(len(pyramide)):
    for j in range(len(pyramide[i])):
        pyramide[i][j] = int(pyramide[i][j])
