found = False
i = 0
while found == False:
    i += 1
    digits1 = list(str(i))
    digits1.sort()
    matching = True
    j = 2
    while matching == True and j <= 6:
        digitsn = list(str(i * j))
        digitsn.sort()
        j += 1
        if digitsn != digits1:
            matching = False
    if matching == True:
        found = True
print(i - 1)
