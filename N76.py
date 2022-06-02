def ultimoscarso(tabella,M,N):
    cont=0
    cont2=1000
    cantante=0
    for i in range(N):
        for j in range(M):
            cont+=int(tabella[i][j])
        if cont<=cont2:
            cont2=cont
            cantante=i
            cont=0
        else:
            cont=0
        return cantante
def giudicebuono(tabella,M,N):
    contT=0
    contD=0
    giudice=0
    for i in range(M):
        for j in range(N):
            if tabella[i][j]>5:
                contT+=1
        if contT>=contD:
            contD=contT
            giudice=i
            contT=0
        else:
            contT=0
    return giudice
def creatabella(M,N):
    tabella=[]
    for i in range(M):
        tabella.append([])
        for j in range(N):
            tabella[i].append(int(input()))
    return tabella
def main():
    M=int(input())
    N=int(input())
    tabella=creatabella(M, N)
    print(giudicebuono(tabella, M, N),ultimoscarso(tabella, M, N))
main()