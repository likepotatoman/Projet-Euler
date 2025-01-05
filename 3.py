def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def prime(n):
    prime = 0
    for i in range(n):
        prime += 1
        while is_prime(prime) == False:
            prime += 1
    return prime

def largest_prime_factor(n):
    prime_index = 2
    while n > 1 :
        while n % prime(prime_index) == 0:
            n = n / prime(prime_index)
        prime_index += 1
        if  prime_index % 100 == 0:
            print("avoid time out")
    return prime(prime_index - 1)

print(largest_prime_factor(600851475143))
