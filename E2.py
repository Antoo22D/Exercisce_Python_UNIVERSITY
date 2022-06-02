def nonogram(mat,ncol,nrig):
    bul=True
    
def creamatrice(n):
    mat=[]
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(int(input()))
    return mat
def main():
    n=int(input())
    mat=creamatrice(n)
    ncol=[]
    nrig=[]
    for c in range(n):
        ncol.append(int(input()))
    for r in range(n):
        nrig.append(int(input()))
main()