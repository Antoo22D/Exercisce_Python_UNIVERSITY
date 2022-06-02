def copie(mat,i,j):
    for i in range(len(mat)-1):
        if mat[i]==mat[i+1]:
            return False
        elif mat[i][j]==mat[i][j+1]:
            return False
        else:
            return True
def main():
    n=int(input())
    mat=[]
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(int(input()))
    if copie(mat,0,0):
        print("SI",end="")
    else:
        print("NO",end="")
main()