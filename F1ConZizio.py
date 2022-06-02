def main(a,b):
    s1=0
    s2=0
    cont=a
    lista=[a]
    mybool=False
    while cont<b:
        lista.append(cont+1)
        cont+=1
    for k in range(len(lista)):
        v1=lista[k]
        for z in range(len(lista)):
            v2=lista[z]
            if z!=k:
                for i in range(2,v1//2+1):
                    if (v1%i)==0:
                        s1+=i
                for j in range(2,v2//2+1):
                    if (v2%j)==0:
                        s2+=j 
                if v1==s2 and v2==s1:
                    mybool=True
                    break
                s1=0
                s2=0
    if mybool==False:
        print("NO",end="")
    else:
        print("SI",end="")
a=int(input())
b=int(input())
main(a,b)