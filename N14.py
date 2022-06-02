seq=""
errore=0
stop=0
while stop!=-1:
    x=int(input())
    if x!=-1:
        if x>=0 and x<=9:
            seq+=str(x)
        else:
            errore+=1
    else:
        stop=-1
if errore!=0:
    print("ERRORE",end="")
elif len(seq)==0:
    print("VUOTO",end="")
else:
    if int(seq)%3==0:
        print(seq)
        print("SI",end="")
    else:
        print(seq)
        print("NO",end="")