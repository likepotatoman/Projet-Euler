#A noter que je ne connaissais pas l'interpretation visuelle des cross-product quand j'ai debute donc j'ai ete aide dans l'elaboration de ce programme
with open("C:/Users/dmlam/Desktop/102_euler.txt", "r") as file:
    raw_data = file.read()
    maps = raw_data.splitlines()

holder_coordinates = []
for i in range(len(maps)):
    holder_coordinates.append(maps[i].split(","))

coordinates = []
for i in range(len(holder_coordinates)):
    coordinates.append([])
    for j in range(len(holder_coordinates[i])):
        coordinates[i].append(int(holder_coordinates[i][j]))

print(coordinates)

def contains_origin(coordinates):
    A, B, C = coordinates[:2], coordinates[2:4], coordinates[4:6]
    AB = [B[0] - A[0], B[1] - A[1]]
    BA = [A[0] - B[0], A[1] - B[1]]
    AC = [C[0] - A[0], C[1] - A[1]]
    AO = [-A[0], -A[1]]
    CO = [-C[0], -C[1]]
    BC = [C[0] - B[0], C[1] - B[1]]
    CB = [B[0] - C[0], B[1] - C[1]]
    BO = [-B[0], -B[1]]
    
    def cross(v1, v2):
        return v1[0] * v2[1] - v1[1] * v2[0]
    
    cross1 = cross(AB, AO)
    cross1_prime = cross(AB, AC)
    if (cross1 > 0 and cross1_prime < 0) or (cross1 < 0 and cross1_prime > 0):
        return False
    
    cross2 = cross(BC, BO)
    cross2_prime = cross(BC, BA)
    if (cross2 > 0 and cross2_prime < 0) or (cross2 < 0 and cross2_prime > 0):
        return False
    
    cross3 = cross(AC, CO)
    cross3_prime = cross(AC, CB)
    if (cross3 > 0 and cross3_prime < 0) or (cross3 < 0 and cross3_prime > 0):
        return False
    return True

    

total = 0
for i in range(len(coordinates)):
    if contains_origin(coordinates[i]):
        print(coordinates[i])
        total += 1
print(total)
