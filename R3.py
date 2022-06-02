def diagIterat(mat):
    somma=0
    j=len(mat)-1
    for i in range(len(mat)):
        somma+=mat[i][j]
        j-=1
    return somma
def diagRicor(mat,i,j):
    if i>=len(mat)and j<=0:
        return 0
    return mat[i][j]+diagRicor(mat, i+1, j-1)
def main():
    N=int(input())
    mat=[]
    for i in range(N):
        mat.append([])
        for j in range(N):
            mat[i].append(int(input()))
    print(diagRicor(mat, 0, len(mat)-1),";", diagIterat(mat),end="")
main()