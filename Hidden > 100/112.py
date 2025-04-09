n_bouncy = 0
n_not_bouncy = 100
i = 101

def bouncy(n):
    n_list = [int(i) for i in list(str(n))]
    if n_list[0] < n_list[-1]:
        for i in range(1, len(n_list)):
            if n_list[i] < n_list[i - 1]:
                return True
    else:
        for i in range(1, len(n_list)):
            if n_list[i] > n_list[i - 1]:
                return True
    return False

while (n_bouncy / (n_bouncy + n_not_bouncy)) < 0.99:
    if bouncy(i):
        n_bouncy += 1
    else:
        n_not_bouncy += 1
    i += 1
print(i - 1)
