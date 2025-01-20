import math
digits = ""
for i in range(1000001):
    digits += str(i)
print(math.prod([int(digits[10**j]) for j in range(7)]))
