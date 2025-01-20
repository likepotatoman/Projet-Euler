data = #it takes a lot of space so I didn't include the data file in the code

def find_relevant_tn():
    values_of_tn = set()
    i = 1
    tn = 1
    while tn <= 364:
        values_of_tn.add(int(tn))
        i += 1
        tn = 0.5 * i * (i + 1)
    return values_of_tn

def letter_position(letter):
    letter = letter.lower()
    return ord(letter) - ord('a') + 1 if 'a' <= letter <= 'z' else -1

tn = find_relevant_tn()

total = 0
for word in data:
    if sum([letter_position(letter) for letter in word]) in tn:
        total += 1
print(total)
