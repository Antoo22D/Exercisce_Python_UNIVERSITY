A=[]
B=[]
nascosta=""
#creo la lista di caratteri A
for i in range(26):
    A.append(input())
    
N=int(input())
#creo la lista di numeri B
for j in range(N):
    B.append(int(input()))
    
#leggo la lista e per ogni valore compreso tra © e 26 prendo il valore della lista A
for j in range(len(B)):
    if B[j]>=0 and B[j]<26:
        nascosta+=str(A[B[j]])    
print(nascosta,end="")