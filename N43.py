'''def parentesizzata(parentesiAperta,parentesiChiusa,espressione,totale,nonparentes):
    for i in range(len(espressione)):
        if espressione[i]=="(":
            totale+=1
        elif espressione[i]==")":
            totale+= -1
        if totale<0:
            nonparentes=True
        return nonparentes
    if totale==0 and not nonparentes:
        return True
    else:
        return False
def superflue(espressione,superfluo):
    for i in range(len(espressione)):    
        if i<len(espressione)-1:
            if espressione[i]=="(" and espressione[i+1]==")":
                superfluo=True
        if not superfluo:
            return True
        else:
            return False
def main():
    espressione=str(input())
    parentesiAperta=0
    parentesiChiusa=0
    totale=0
    nonparentes=False
    superluo=False
    superff=superflue(i, espressione, superfluo)
    pare=parentesizzata(parentesiAperta, parentesiChiusa, espressione, totale, nonparentes)
    if superff:
        print("ok1",end="")
    else:
        print("no1",end="")
    if pare:
        print("ok2",end="")
    else:
        print("no2",end="")
main()
'''
#1 ben parentesizzata
parentesiAperte = 0
parentesiChiuse = 0
totParentesi = 0
NONPARENTESIZZATA = False
#2 nessuna coppia di parentesi superflua
SUPERFLUO = False

equazione = str(input())
for i in range(len(equazione)):
    #1
    if equazione[i] == '(':
        totParentesi += 1
    elif equazione[i] == ')':
        totParentesi += -1

    if totParentesi < 0:
        NONPARENTESIZZATA = True
    #2
    if i<len(equazione)-1:
        if equazione[i] == '(' and equazione[i+1] == ')':
            SUPERFLUO = True
if totParentesi == 0 and not NONPARENTESIZZATA:
    print("ok1")
else:
    print("no1")

if not SUPERFLUO:
    print("ok2")
else:
    print("no2")