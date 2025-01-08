from google.colab import files
uploaded = files.upload()
with open("67_euler.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()

pyramide = []
for i in range(len(lines)):
    line = lines[i].split(" ")
    pyramide.append(line)
print(pyramide)

for i in range(len(pyramide)):
    for j in range(len(pyramide[i])):
        if pyramide[i][j][0] == "0":
            pyramide[i][j] = int(pyramide[i][j][1])
        else : 
            pyramide[i][j] = int(pyramide[i][j])



def resolve(pyramide):
    if len(pyramide) == 1:
        return pyramide[0]
    for i in range(len(pyramide[-2])):
        if pyramide[-1][i] > pyramide[-1][i + 1]:
            pyramide[-2][i] += pyramide[-1][i]
        else : 
            pyramide[-2][i] += pyramide[-1][i + 1]
    pyramide.pop(-1)
    return resolve(pyramide)

print(resolve(pyramide))
