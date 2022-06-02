X=int(input())
lista=[]
pari=[]
dispari=[]
par=True
dis=True

for i in range(X):
    z=int(input())
    lista.append(z)

for j in range(len(lista)):
    if j==0 or j%2==0:
        pari.append(lista[j])
    else:
        dispari.append(lista[j])
        
for k in dispari:
    if k%2!=0:
        dis=True
    else:
        dis=False
        break
vTemporanea=""
for l in pari:
    if vTemporanea == "":
        vTemporanea = l
    else:
        if l > vTemporanea:
            par = True
        else:
            par = False
            
if par and dis:
    print("SI",end="")
else:
    print("NO",end="")