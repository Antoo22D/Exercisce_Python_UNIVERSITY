def numesami(mat,n,m):
    listaStud=[]
    somma=0
    media=0
    for i in range(n):
        listaStud.append(mat[i].count(0))
    massimo=list(mat[listaStud.index(min(listaStud))])
    for k in range(len(massimo)):
        if massimo[k]!=0:
            somma+=massimo[k]
            media+=1
    return round(somma/media)
def nessuno(mat,n,m):
    trovato=0
    no18=0
    for i in range(m):
        for j in range(n):
            if mat[i][j]==18:
                trovato+=1
        if trovato==0:
            no18+=1
        trovato=0
    return no18
def main():
    n=int(input())
    m=int(input())
    mat=[]
    for i in range(n):
        mat.append([])
        for j in range(m):
            mat[i].append(int(input()))
    print(nessuno(mat, n, m),numesami(mat, n, m))
main()