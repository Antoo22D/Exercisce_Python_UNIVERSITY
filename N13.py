n=int(input())
m=int(input())
sonoPrimi=True

for i in range(2,abs(n)):
    if n%i==0:
        sonoPrimi=False
        break
    
for i in range(2,abs(m)):
    if m%i==0:
        sonoPrimi=False
        break
if sonoPrimi==True:
    if abs(m-n)==2:
        print("gemelli")
    else:
        print("non gemelli")
else:
    print("non entrambi priimi")