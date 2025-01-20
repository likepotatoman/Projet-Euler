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

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


maxi = 0
for k in range(10, 0, -1):
    for perm in permutation([i for i in range(1,k)]):
        int_perm = ""
        for i in range(len(perm)):
            int_perm += str(perm[i])
        int_perm = int(int_perm)
        
        if int_perm > maxi:
            if is_prime(int_perm):
                maxi = int_perm
print(maxi)
