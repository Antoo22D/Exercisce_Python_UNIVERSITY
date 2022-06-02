a=int(input())
b=int(input())
lista1=[a]               #numeri intervallo [A,B]
cont=a
bul=True
bul2=True
somma=0
somma2=0
while cont<b:
    lista1.append(cont+1)
    cont+=1
for i in lista1:
    for j in lista1:
        if lista1.index(i)!=lista1.index(j) and lista1.index(i)<lista1.index(j):
            for o in range(2,i):
                if  i%o==0:
                    somma+=o
            if somma!=b:
                bul=False
            somma=0
            for z in range(2,j):
                if  j%z==0:
                    somma2+=z
            if somma2!=a:
                bul2=False
            somma2=0
if bul and bul2:
    print("SI",end="")
else:
    print("NO",end="")