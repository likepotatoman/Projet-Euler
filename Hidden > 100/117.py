import math

def fact(n):
    return math.prod([i for i in range(1, n + 1)])

def comb(n, k):
    def fact(n):
        return math.prod([i for i in range(1, n + 1)])
    return fact(n) / (fact(k) * fact(n - k))

def arreng(n, k):
    def fact(n):
        return math.prod([i for i in range(1, n + 1)])
    return fact(n) / fact(n - k)    

n_units = 50
total = 0


#reds, length = 2
for red in range(n_units // 2 + 1):

    #green, length = 3
    for green in range((n_units - 2 * red) // 3 + 1):
        
        #blue, length = 4
        for blue in range((n_units - 2 * red - 3 * green) // 4 + 1):
            
            #print(red, green, blue, arreng((n_units - red - 2 * green - 3 * blue), (red + blue + green)) / (fact(red) * fact(green) * fact(blue)))

            #in this case we do an arrang because the order is important. We then divide by the fact of each individually because G1,R,G2 == G2,R,G1 for example
            total += arreng((n_units - red - 2 * green - 3 * blue), (red + blue + green)) / (fact(red) * fact(green) * fact(blue)) 


print(total)
