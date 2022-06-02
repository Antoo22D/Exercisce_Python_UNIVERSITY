cont9 = 0
cont3 = 0
contR = 0
vTemp = -1
while cont9 != 3:
    x = int(input())
    if x >= 0 and x < 10:
        if x == 9:
            if cont9 == 2:
                cont9 += 1
            else:
                vTemp = x
                cont9 += 1
        else:
            cont9 = 0
            if x == vTemp:
                if cont3 == 2:
                    contR += 1
                else:
                    cont3 += 1
            else:
                vTemp = x
                cont3 = 1
    else:
        cont9 = 0
        cont3 = 0
print(contR, end="")
