def palindrome(n):
    n = str(n)
    first_half = n[:len(n) // 2]

    if len(n) % 2 == 0:
        second_half = n[len(n) // 2:]
    else : 
        second_half = n[len(n) // 2 + 1:]
    
    first_half = list(first_half)
    second_half = list(second_half)
    second_half.reverse()

    if second_half == first_half :
        return True
    return False

def largest_3_digit_palindrome():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if palindrome(i * j) and i*j > largest:
                largest = i * j
    return largest

print(largest_3_digit_palindrome())
