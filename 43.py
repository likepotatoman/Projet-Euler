#I know I don't need to check for permutations from 1 to 8 or 1 to 9 as they are both always divisible by 3 but I still did it
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

#j'avais mal compris le principe de sub-string donc ce n'est pas tres beau mais je pourrais le farie plus beau
total = 0
for perm in permutation([i for i in range(10)]):
    Flag = True
    if int(str(perm[1]) + str(perm[2]) + str(perm[3])) % 2 != 0:
        Flag = False
    if int(str(perm[2]) + str(perm[3]) + str(perm[4])) % 3 != 0:
        Flag = False
    if int(str(perm[3]) + str(perm[4]) + str(perm[5])) % 5 != 0:
        Flag = False
    if int(str(perm[4]) + str(perm[5]) + str(perm[6])) % 7 != 0:
        Flag = False
    if int(str(perm[5]) + str(perm[6]) + str(perm[7])) % 11 != 0:
        Flag = False
    if int(str(perm[6]) + str(perm[7]) + str(perm[8])) % 13 != 0:
        Flag = False
    if int(str(perm[7]) + str(perm[8]) + str(perm[9])) % 17 != 0:
        Flag = False
    
    if Flag == True:
        int_perm = ""
        for i in range(len(perm)):
            int_perm += str(perm[i])
        int_perm = int(int_perm)
        total += int_perm
print(total)
