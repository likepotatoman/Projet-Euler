def finder():
    i = 1
    while True:
        if i % 1000000 == 0:
            print("avoid time out")
        found = True
        for j in range(1,21):
            if found == True:
                if i % j != 0:
                    found = False
        if found == True:
            return i
        i += 1

print(finder())
#force brute absolue
