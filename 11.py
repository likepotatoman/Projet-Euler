from google.colab import files
uploaded = files.upload()
with open("9_euler.txt", "r") as file:
    content = file.read()
lines = content.splitlines()
matrice = []
for i in range(len(lines)):
    new_line = lines[i].split(' ')
    matrice.append(new_line)
true_max = 0

def check_line(line):
    max = 0

    if len(line) >= 4:
        for i in range(len(line) - 3):
            if int(line[i]) * int(line[i + 1]) * int(line[i + 2]) * int(line[i + 3]) > max:
                max = int(line[i]) * int(line[i + 1]) * int(line[i + 2]) * int(line[i + 3])

    return max

def rotate(matrice):
    rotated_matrice = []
    for i in range(len(matrice[0])):
        rotated_matrice.append([])
        for j in range(len(matrice)):
            rotated_matrice[i].append(matrice[len(matrice) - j - 1][i])
    return rotated_matrice

def flip(matrice):
    flipped_matrice = []
    for i in range(len(matrice)):
        line = list(matrice[i])
        line.reverse()
        flipped_matrice.append(line)
    return flipped_matrice

def diagonal_read(matrice):
    diagonal_read_matrice = []
    for i in range(len(matrice)):
        line = []
        j = i
        k = 0
        while j >= 0:
            line.append(matrice[j][k])
            k += 1
            j -= 1
        diagonal_read_matrice.append(line)
    
    for i in range(1,len(matrice[0])):
        line = []
        j = len(matrice) - 1
        k = i
        while k < len(matrice[0]):
            line.append(matrice[j][k])
            k += 1
            j -= 1
        diagonal_read_matrice.append(line)
    return diagonal_read_matrice
    

#de la gauche
test_matrice = matrice
for i in range(len(matrice)):
    if true_max < check_line(test_matrice[i]):
        true_max = check_line(test_matrice[i])

#du haut
test_matrice = flip(rotate(matrice))
for i in range(len(matrice)):
    if true_max < check_line(test_matrice[i]):
        true_max = check_line(test_matrice[i])

#du diagonal haut gauche
test_matrice = diagonal_read(matrice)
for i in range(len(test_matrice)):
    if true_max < check_line(test_matrice[i]):
        true_max = check_line(test_matrice[i])

#du diagonal haut droit
test_matrice = diagonal_read(rotate(matrice))
for i in range(len(test_matrice)):
    if true_max < check_line(test_matrice[i]):
        true_max = check_line(test_matrice[i])

print(true_max)
