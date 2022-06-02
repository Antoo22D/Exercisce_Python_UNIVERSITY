def controlla(miaseq):
    prec = ""
    cons=0    
    for i in miaseq:
        if prec.islower() and i.islower() and prec==i:
            cons+=1
            prec=i
        elif i.isupper() and prec.isupper():
            cons += 1
            prec = i
        else:
            prec = i
    if cons>0:
        return True
    return False
def main():
    seq=input()
    miaseq=[]
    while seq!="*":
        miaseq.append(seq)
        seq=input()
    if controlla(alf, miaseq):
        print("SI",end="")
    else:
        print("NO",end="")
main()