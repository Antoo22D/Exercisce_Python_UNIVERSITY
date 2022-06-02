def creamat(n,m):
    mat=[]
    for i in range(n):
        mat.append([])
        for j in range(m):
            mat.append(input())
    return mat
def main():
    n=int(input("N: "))          #righe
    m=int(input("M: "))          #colonne
    k=int(input("K: "))
    elencoK=[]
    mat=creamat(n, m)
    for z in range(k):
        elencoK.append(input())
    print(mat,end="")
main()