#This is my first dijkestra implementation ever so forgive the, most-likely, ugly code
with open("C:/Users/dmlam/Desktop/81_euler.txt", "r") as file:
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

#implementing dijkestra in a 2D plane
def dijkstra_implementation(matrix, minimal_path_yet = [ [[0,0], matrix[0][0]] ], true_minimal_path = []): #the format is position, score, previous_position
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
                minimal_path_yet.append([[previous_position_position[0], previous_position_position[1] + 1], previous_position_score + matrix[previous_position_position[0]][previous_position_position[1] + 1], previous_position_position])
            else:
                if previous_position_score + matrix[previous_position_position[0]][previous_position_position[1] + 1] < [path[1] for path in minimal_path_yet if path[0] == [previous_position_position[0], previous_position_position[1] + 1]][0]:
                    for i in range(len(minimal_path_yet)):
                        if minimal_path_yet[i][0] == [previous_position_position[0], previous_position_position[1] + 1]:
                            index = i
                    minimal_path_yet.pop(index)
                    minimal_path_yet.append([[previous_position_position[0], previous_position_position[1] + 1], previous_position_score + matrix[previous_position_position[0]][previous_position_position[1] + 1], previous_position])

    #go down
    if previous_position_position[0] < len(matrix) - 1:
        if [previous_position_position[0] + 1, previous_position_position[1]] not in [path[0] for path in true_minimal_path]:
            if [previous_position_position[0] + 1, previous_position_position[1]] not in [path[0] for path in minimal_path_yet]:
                minimal_path_yet.append([[previous_position_position[0] + 1, previous_position_position[1]], previous_position_score + matrix[previous_position_position[0] + 1][previous_position_position[1]], previous_position_position])
            else:
                if previous_position_score + matrix[previous_position_position[0] + 1][previous_position_position[1]] < [path[1] for path in minimal_path_yet if path[0] == [previous_position_position[0] + 1, previous_position_position[1]]][0]:
                    for i in range(len(minimal_path_yet)):
                        if minimal_path_yet[i][0] == [previous_position_position[0] + 1, previous_position_position[1]]:
                            index = i
                    minimal_path_yet.pop(index)
                    minimal_path_yet.append([[previous_position_position[0] + 1, previous_position_position[1]], previous_position_score + matrix[previous_position_position[0] + 1][previous_position_position[1]], previous_position])

    return true_minimal_path

corner_found = False
while corner_found == False:
    
    confirmed_paths = dijkstra_implementation(matrix)
    if len(confirmed_paths) % 1000 == 0:
        print(str(len(confirmed_paths)) + " confirmed paths")
    if [len(matrix) - 1, len(matrix[0]) - 1] in [path[0] for path in confirmed_paths]:
        corner_found = True

for i in range(len(confirmed_paths)):
    if confirmed_paths[i][0] == [len(matrix) - 1, len(matrix[0]) - 1]:
        print(confirmed_paths[i][1])
