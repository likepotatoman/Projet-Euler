#Tried solving it without making a matrix and it worked quite well
#I noticed a pattern so I tried to see if it would work : it did
total = 1
i = 1
num_to_add = 2
while i < 1001 * 1001:
    for j in range(4):
        i += num_to_add
        total += i
    num_to_add += 2
print(total)
