#it could be interesting to implement caching but brute forcing works for under 1000000
import math
def factorial(n):
    return math.prod([i+1 for i in range(n)])
    
total = 0
for i in range(1000000):
    if i % 10000 == 0:
        print("looped")
    previous_numbers = set()
    current_number = i
    while current_number not in previous_numbers:
        previous_numbers.add(int(current_number))
        current_number = sum([factorial(int(j)) for j in str(current_number)])
    if len(previous_numbers) == 60:   
        total += 1
print(total)
