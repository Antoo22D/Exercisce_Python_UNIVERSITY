import random
from random import randint

random.seed(0)
contUtente=0
contPc=0

while (contUtente<3 and contPc<3):
    manoU=int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice--> "))
    if (manoU==1):
        print("Hai giocato sasso")
        manoPc=random.randint(1, 3)
        if manoPc==3:
            print("Il pc ha giocato forbice")
            print("Vinci tu!")
            contUtente+=1
            print(contUtente,"-",contPc,sep="")
        if manoPc==2:
            print("Il pc ha giocato carta")
            print("Vince il pc")
            contPc+=1
            print(contUtente,"-",contPc,sep="")
        if manoPc==1:
            print("Il pc ha giocato sasso")
            print("PARI")
            print(contUtente,"-",contPc,sep="")
    if (manoU==2):
        print("Hai giocato carta")
        manoPc=random.randint(1, 3)
        if manoPc==3:
            print("Il pc ha giocato forbice")
            print("Vince il pc")
            contPc+=1
            print(contUtente,"-",contPc,sep="")
        if manoPc==2:
            print("Il pc ha giocato carta")
            print("PARI!")
            print(contUtente,"-",contPc,sep="")
        if manoPc==1:
            print("Il pc ha giocato sasso")
            print("Hai vinto tu!")
            contUtente+=1
            print(contUtente,"-",contPc,sep="")
    if (manoU==3):
        print("hai giocato forbice")
        manoPc=random.randint(1,3)
        if(manoPc==3):
            print("il PC ha giocato forbice")
            print("Pari:")
            print(contUtente,"-",contPc,sep="")
        if(manoPc==2):
            print("il PC ha giocato carta")
            print("Vinci tu:")
            contg+=1
            print(contUtente,"-",contPc,sep="")
        if(manoPc==1):
            print("il PC ha giocato sasso")
            print("Vince il PC:")
            contPc+=1
            print(contUtente,"-",contPc,sep="")
if contPc==3:
    print("IL PC HA VINTO LA SFIDA")
else:
    print("HAI VINTO LA SFIDA!!")