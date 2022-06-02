def diagSec(mat,i,j):
    if i>=len(mat) and j<0:
        return 0
    return mat[i][j]+diagSec(mat, i+1, j-1)
def riempi(mat,x):
    inserito=1
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j]=inserito
            inserito+=1
            if inserito==x+1:
                inserito=1
    return mat
def creamatrice(n):
    mat=[]
    for z in range(n):
        mat.append([0]*n)
    return mat
def main():
    x=int(input())
    mat=creamatrice(10)
    mat=riempi(mat, x)
    print(diagSec(mat, 0, len(mat)-1),end="")
main()
