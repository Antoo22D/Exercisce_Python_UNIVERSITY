'''def main():
    k=int(input())
    a=[]
    for i in range(k):
        a.append(int(input()))
    nRig=int(input())
    mCol=int(input())
    b=[]
    for j in range(nRig):
        b.append([0]*mCol)
    riga=0
    colonna=0
    numeri=0 
main()
'''
K = int(input())
A = []
for i in range(K):
    A.append(int(input()))
N = int(input())
M = int(input())
#CREO LA MIA MATRICE
B = []
for j in range(N):
    B.append([0]*M)
riga = 0
colonna = 0
numeri = 0
while(riga < N and colonna < M):
    for i in range(colonna, M):
        B[riga][i] = A[numeri]
        if numeri+1 >= len(A):
            numeri = 0
        else:
            numeri += 1
    riga += 1
    for i in range(riga, N):
        B[i][M-1] = A[numeri]
        if numeri+1 >= len(A):
            numeri = 0
        else:
            numeri += 1
    M -= 1
    if(riga < N):
        for i in range(M-1, colonna-1, -1):
            B[N-1][i] = A[numeri]
            if numeri+1 >= len(A):
                numeri = 0
            else:
                numeri += 1
        N -= 1
    if(colonna < riga):
        for i in range(N-1, riga-1, -1):
            B[i][colonna] = A[numeri]
            if numeri+1 >= len(A):
                numeri = 0
            else:
                numeri += 1
        colonna += 1
stringa = ""
for i in range(len(B)):
    for j in range(len(B[i])):
        stringa += str(B[i][j])
    print(stringa)
    stringa = ""