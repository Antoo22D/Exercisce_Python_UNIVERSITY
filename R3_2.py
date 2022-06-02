def sommaNONricorsiva(mat):
    somma=0
    j=len(mat)-1
    for i in range(len(mat)):
        somma+=mat[i][j]
        j-=1
    return somma
def sommaRICORSIVA(mat,r,c):
    if r>=len(mat) and c<=0:
        return 0
    return sommaRICORSIVA(mat, r+1, c-1)

def creamat(n):
    mat=[]
    for r in range(n):
        mat.append([])
        for c in range(n):
            mat[r].append(int(input()))
    return mat
def main():
    n=int(input())
    mat=creamat(n)
    print(sommaRICORSIVA(mat, 0, len(mat)-1),";",sommaNONricorsiva(mat),end="")
main()