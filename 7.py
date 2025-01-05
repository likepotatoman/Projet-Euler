def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def prime(n):
    prime = 1
    for i in range(n):
        if i % 100 == 0:
            print("avoid time out")
        prime += 1
        while is_prime(prime) == False:
            prime += 1
    return prime

print(prime(10001))
