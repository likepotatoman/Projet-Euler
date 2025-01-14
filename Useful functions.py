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
    factors = {1, n}
    for i in range(2,round(np.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(int(n / i))
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

#gives the alphabetical position of a letter
def letter_position(letter):
    return ord(letter.lower()) - ord('a') + 1

#gives the n-th fibonacci number, first time I have implemented a cache by hand
def fib(n, fib_answers = {1 : 1, 2 : 1}):
    if n in fib_answers:
        return fib_answers[n]
    fib_answer = fib(n - 1) + fib(n - 2)
    fib_answers[n] = fib_answer
    return fib_answer

#gives the list of all permutations of the elements given
def permutation(remaining_elements, fixed_elements = []):
    if len(remaining_elements) == 0:
        return fixed_elements
    permutations = []
    for i in range(len(remaining_elements)):
        new_remaining_elements = list(remaining_elements)
        new_remaining_elements.remove(remaining_elements[i])
        new_fixed_elements = list(fixed_elements)
        new_fixed_elements.append(remaining_elements[i])
        permutations.append(permutation(new_remaining_elements, new_fixed_elements))
    def flatten(liste):
        flattened = []
        for item in liste:
            if isinstance(item, list):
                if isinstance(item[0], list):
                    flattened.extend(flatten(item))
                else:
                    flattened.append(item)
        return flattened
    return flatten(permutations)

#flattens n-depth lists into it's base constituants, if one wishes to return the base lists, he has to add another condition to check if the inside of the list is not the base constituants as done in permutation()
def flatten(liste):
    flattened = []
    for item in liste:
        if tisinstance(item, list):
            flattened.extend(flatten(item)) 
        else:
            flattened.append(item)
    return flattened

#converts n in base 10 into base p
def chiffre(p, b):
    liste_reponse = ""
    plus_grande_puissance = 0
    while b**(plus_grande_puissance + 1) <= p:
        plus_grande_puissance += 1
    for i in range(plus_grande_puissance,-1,-1):
        c = 0
        while b**i <= p:
            c += 1
            p = p - b**i
        liste_reponse += str(c)
    return int(liste_reponse)
