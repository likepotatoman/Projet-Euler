import sys
sys.setrecursionlimit(100000)  # Increase the recursion limit

from google.colab import files
uploaded = files.upload()

with open("81_euler.txt", "r") as file: #81 and 82 are the same matrix
    content = file.read()
    lines = content.splitlines()
holder = []
for i in range(len(lines)):
    line = lines[i].split(",")
    holder.append(line)
matrix = []
for i in range(len(holder)):
    matrix.append([])
    for j in range(len(holder[i])):
        matrix[i].append(int(holder[i][j]))

def dijkstra_implementation(matrix, minimal_path_yet, true_minimal_path): #the format is position, score, previous_position
    #break condition
    for i in range(len(true_minimal_path)):
        if true_minimal_path[i][0] == [len(matrix[0]) - 1, len(matrix) - 1]:
            print()
            return true_minimal_path[i][1]
    
    
    minimum_score_position_index = 0
    for i in range(len(minimal_path_yet)):
        if minimal_path_yet[i][1] < minimal_path_yet[minimum_score_position_index][1]:
            minimum_score_position_index = i
    
    previous_position_position = list(minimal_path_yet[minimum_score_position_index][0])
    previous_position_score = int(minimal_path_yet[minimum_score_position_index][1])
    
    true_minimal_path.append(minimal_path_yet[minimum_score_position_index])
    minimal_path_yet.pop(minimum_score_position_index)
    
    #go right
    if previous_position_position[1] < len(matrix[0]) - 1:
        if [previous_position_position[0], previous_position_position[1] + 1] not in [path[0] for path in true_minimal_path]:
            if [previous_position_position[0], previous_position_position[1] + 1] not in [path[0] for path in minimal_path_yet]:
                minimal_path_yet.append([[previous_position_position[0], previous_position_position[1] + 1], previous_position_score + matrix[previous_position_position[0]][previous_position_position[1] + 1]])
            else:
                if previous_position_score + matrix[previous_position_position[0]][previous_position_position[1] + 1] < [path[1] for path in minimal_path_yet if path[0] == [previous_position_position[0], previous_position_position[1] + 1]][0]:
                    for i in range(len(minimal_path_yet)):
                        if minimal_path_yet[i][0] == [previous_position_position[0], previous_position_position[1] + 1]:
                            index = i
                    minimal_path_yet.pop(index)
                    minimal_path_yet.append([[previous_position_position[0], previous_position_position[1] + 1], previous_position_score + matrix[previous_position_position[0]][previous_position_position[1] + 1]])

    #go left
    if previous_position_position[1] > 0:
        if [previous_position_position[0], previous_position_position[1] - 1] not in [path[0] for path in true_minimal_path]:
            if [previous_position_position[0], previous_position_position[1] - 1] not in [path[0] for path in minimal_path_yet]:
                minimal_path_yet.append([[previous_position_position[0], previous_position_position[1] - 1], previous_position_score + matrix[previous_position_position[0]][previous_position_position[1] - 1]])
            else:
                if previous_position_score + matrix[previous_position_position[0]][previous_position_position[1] - 1] < [path[1] for path in minimal_path_yet if path[0] == [previous_position_position[0], previous_position_position[1] - 1]][0]:
                    for i in range(len(minimal_path_yet)):
                        if minimal_path_yet[i][0] == [previous_position_position[0], previous_position_position[1] - 1]:
                            index = i
                    minimal_path_yet.pop(index)
                    minimal_path_yet.append([[previous_position_position[0], previous_position_position[1] - 1], previous_position_score + matrix[previous_position_position[0]][previous_position_position[1] - 1]])



    #go down
    if previous_position_position[0] < len(matrix) - 1:
        if [previous_position_position[0] + 1, previous_position_position[1]] not in [path[0] for path in true_minimal_path]:
            if [previous_position_position[0] + 1, previous_position_position[1]] not in [path[0] for path in minimal_path_yet]:
                minimal_path_yet.append([[previous_position_position[0] + 1, previous_position_position[1]], previous_position_score + matrix[previous_position_position[0] + 1][previous_position_position[1]]])
            else:
                if previous_position_score + matrix[previous_position_position[0] + 1][previous_position_position[1]] < [path[1] for path in minimal_path_yet if path[0] == [previous_position_position[0] + 1, previous_position_position[1]]][0]:
                    for i in range(len(minimal_path_yet)):
                        if minimal_path_yet[i][0] == [previous_position_position[0] + 1, previous_position_position[1]]:
                            index = i
                    minimal_path_yet.pop(index)
                    minimal_path_yet.append([[previous_position_position[0] + 1, previous_position_position[1]], previous_position_score + matrix[previous_position_position[0] + 1][previous_position_position[1]]])
    
    #go up
    if previous_position_position[0] > 0:
        if [previous_position_position[0] - 1, previous_position_position[1]] not in [path[0] for path in true_minimal_path]:
            if [previous_position_position[0] - 1, previous_position_position[1]] not in [path[0] for path in minimal_path_yet]:
                minimal_path_yet.append([[previous_position_position[0] - 1, previous_position_position[1]], previous_position_score + matrix[previous_position_position[0] - 1][previous_position_position[1]]])
            else:
                if previous_position_score + matrix[previous_position_position[0] - 1][previous_position_position[1]] < [path[1] for path in minimal_path_yet if path[0] == [previous_position_position[0] - 1, previous_position_position[1]]][0]:
                    for i in range(len(minimal_path_yet)):
                        if minimal_path_yet[i][0] == [previous_position_position[0] - 1, previous_position_position[1]]:
                            index = i
                    minimal_path_yet.pop(index)
                    minimal_path_yet.append([[previous_position_position[0] - 1, previous_position_position[1]], previous_position_score + matrix[previous_position_position[0] - 1][previous_position_position[1]]])    
    
    return dijkstra_implementation(matrix, minimal_path_yet, true_minimal_path)

print(dijkstra_implementation(matrix, [ [[0,0], matrix[0][0]] ], []))
