def controllo(mat,i,j):
    for i in range(len(mat)-1):
        if mat[i]==mat[i+1]:
            return False
        else:
            if mat[i][j]==mat[i][j+1]:
                return False
            else:
                return True
def creamat(n):
    mat=[]
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(int(input()))
    return mat
def main():
    n=int(input())
    matrice=creamat(n)
    if controllo(matrice,0,0):
        print("SI",end="")
    else:
        print("NO",end="")
main()