#put some caching that is very similar to what could be used for 74
def arrives_89(starting_number, arrivals = {}):
    current_number = starting_number
    while current_number != 89 and current_number != 1:
        if current_number in arrivals:
            return arrivals[current_number]
        current_number = sum([int(j)**2 for j in str(current_number)])
    arrived_89 = False
    if current_number == 89:
        arrived_89 = True
    arrivals[starting_number] = arrived_89
    return arrived_89

total = 0
for i in range(1,10000000):
    if i % 100000 == 0:
        print(i / 100000)

    if arrives_89(i):
        total += 1
print(total)
