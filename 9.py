import numpy as np
c = 1
stop = False
while c < 1000**2 and stop == False:
    c_carre = c**2
    a = 1
    while a < np.sqrt(c_carre):
        a_carre = a ** 2
        for b in range(a, round(np.sqrt(c_carre))):
            if a + b + c == 1000 and a_carre + b ** 2 == c_carre:
                print(a*b*c)
                stop = True
        a += 1
    c += 1
