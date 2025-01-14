def chiffre(b,p):
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
    return liste_reponse

def is_palindrome(n):
    n = str(n)
    n_reverse = str(n)[::-1]
    if n == n_reverse :
        return True
    return False

print(is_palindrome(585))
print(is_palindrome(chiffre(2,585)))

total = 0
for i in range(1,1000001):
    if is_palindrome(i) and is_palindrome(chiffre(2,i)):
        total += i
print(total)
