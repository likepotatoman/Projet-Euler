import math

def fact(n):
    return math.prod([i for i in range(1, n + 1)])

n_grey_tiles = 50

#calculating the red combinations
red_total = 0
for n_RT in range(1, n_grey_tiles // 2 + 1):
    #we collapse the second tile taken up into one and just take it away from the total number of tiles and then simply use the formula for combinations
    red_total += fact(n_grey_tiles - n_RT) / ( fact(n_RT) * fact(n_grey_tiles - n_RT - n_RT))

#calculating the green combinations
green_total = 0
for n_GT in range(1, n_grey_tiles // 3 + 1):
    #same as for the red but instead of 1 extra tile it is 2 that get collapsed
    green_total += fact(n_grey_tiles - 2 * n_GT) / ( fact(n_GT) * fact(n_grey_tiles - 2 * n_GT - n_GT))
    
blue_total = 0
for n_BT in range(1, n_grey_tiles // 4 + 1):
    #same as green but 3
    blue_total += fact(n_grey_tiles - 3 * n_BT) / ( fact(n_BT) * fact(n_grey_tiles - 3 * n_BT - n_BT))

print(red_total + blue_total + green_total)
