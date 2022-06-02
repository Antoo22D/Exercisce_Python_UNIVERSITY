posti=[0,0,0,0,0,0,0,0,0,0]

while 0 in posti:
    primo=int(input("Digitare 1 per fumatori o 2 per non fumatori:"))
    if primo==1:
        if 0 not in posti[:5]:
            scelta=input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if scelta=="S":
                for i in range(5,11):
                    if posti[i]==0:
                        posti[i]=i+1
                        print("Reparto NON fumatori, posto",i+1)
                        break
            else:
                for i in range(0,5):
                    if posti[i]==0:
                        posti[i]=i+1
                        print("Reparto fumatori, posto", i+1)
                        break
    else:
        if 0 not in posti[5:]:
            y=input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if y=="S":
                for i in range(0,5):
                    if posti[i]==0:
                        posti[i]=i+1
                        print("Reparto fumatori, posto",i+1)
                        break
            else:
                print("Il prossimo volo parte tra 3 ore")
        for i in range(5,10):
            if posti[i]==0:
                posti[i]=i+1
                print("Reparto NON fumatori,posto",i+1)
                break