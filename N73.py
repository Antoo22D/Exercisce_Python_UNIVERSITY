N=int(input())
x=0
numero=str(N)
risul=''
for i in range(len(numero)):
    if i==len(numero)-1:
        x+=1
        risul+=str(x)+numero[i]
    else:
        if numero[i]==numero[i+1]:
            x+=1
        else:
            x+=1
            risul+=str(x)+numero[i]
            x=0
print(risul,len(risul),end="")