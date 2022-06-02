s=input()
n=int(input())
elenco=[]
trovata=False
for i in range(n):
    elenco.append(input())
for j in range(elenco):
    for z in range(elenco):
        if j+z==s:
            trovata=True
if trovata:
    print("OK")
else:
    print(max(Elenco)+min(Elenco),end="")