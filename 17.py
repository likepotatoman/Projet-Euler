import inflect
p = inflect.engine()

total = 0
for i in range(1, 1001):
    total += len(p.number_to_words(i)) - p.number_to_words(i).count(" ") - p.number_to_words(i).count("-")
print(total)
