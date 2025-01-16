#checks if n is prime
def is_prime(n):
    for i in range(2,round(n**0.5) + 1):
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

def spin(num):
    num = str(num)
    return int(num[-1] + num[:-1])

total = 0
for i in range(2,1000001):
    flag = True
    number = i
    for j in range(len(str(i))):
        if not is_prime(number):
            flag = False
            break
        number = spin(number)
    if flag == True:
        total += 1
print(total)
