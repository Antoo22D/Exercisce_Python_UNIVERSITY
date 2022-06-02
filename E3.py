def sottoseq(lista1):
    vTemp=0
    sotss=[]
    for i in range(len(lista1)):
        if i==len(lista1)-1:
            sotss.append(lista1[i])
            if len(sotss)>=2:
                    vTemp+=1
        else:
            if int(lista1[i])+1==int(lista1[i+1]):
                sotss.append(lista1[i])
            else:
                sotss.append(lista1[i])
                if len(sotss)>=2:
                    vTemp+=1
                sotss=[]
    return vTemp
def main():
    sequenza=input()
    lista=[]
    while sequenza!="*":
        lista.append(sequenza)
        sequenza=input()
    print(sottoseq(lista),end="")
main()