def collatz_sequence(previous_numbers):
    if previous_numbers[-1] == 2:
        previous_numbers.append(1)
        return previous_numbers
    if previous_numbers[-1] % 2 == 0:
        previous_numbers.append(int(previous_numbers[-1] / 2))
        return collatz_sequence(previous_numbers)
    else:
        previous_numbers.append(previous_numbers[-1] * 3 + 1)
        return collatz_sequence(previous_numbers)

max_length = 0
for i in range(1, 1000001):
    if len(collatz_sequence([i])) > max_length:
        max_length = len(collatz_sequence([i]))
        best_starting_number = i
        print("avoid time out", str(i))
print(best_starting_number)
