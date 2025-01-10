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
            if isinstance(item, list):  # Check if the item is a list
                if isinstance(item[0], list):
                    flattened.extend(flatten(item))  # Recursively flatten it
                else:
                    flattened.append(item)
        return flattened
    
    return flatten(permutations)

permutations_from_0_to_9 = permutation([0,1,2,3,4,5,6,7,8,9])
lexiconographic_permutations = []
for given_permutation in permutations_from_0_to_9:
    number = ""
    for element in given_permutation:
        number += str(element)
    lexiconographic_permutations.append(int(number))

lexiconographic_permutations.sort()
print(lexiconographic_permutations[999999])
