from functools import cache

@cache
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

somme = 0
i = 0
while fib(i) < 4000000:
    if fib(i) % 2 == 0:
        somme += fib(i)
    i += 1
print(somme)
