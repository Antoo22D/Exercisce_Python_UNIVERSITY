num=int(input())
biglietto=[]
prima=0
seconda=0

for i in str(num):
    biglietto.append(i)
    
    
for j in range(len(biglietto)//2):
    prima+=int(biglietto[j])

for z in range(len(biglietto)//2,len(biglietto)):
    seconda+=int(biglietto[z])
    
if prima==seconda:
    print("FORTUNATO",end="")
else:
    print("SFORTUNATO",end="")