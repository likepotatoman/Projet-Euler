with open("C:/Users/dmlam/Desktop/euler 13.txt", "r") as file:
    content = file.read()
digits = content.splitlines()

print(str(sum([int(digit) for digit in digits]))[:10])
