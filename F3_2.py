def cream(N,M,mat):
    for i in range(N):
        mat.append([])
        for j in range(M):
            mat[i].append(input())
    return mat

def cream2(mat2,N,M):
    for i in range(N):
        mat2.append([])
        for j in range(M):
            mat2[i].append(1)
    return mat2

def creap(par,K):
    for i in range(K):
        par.append(input("Parola di K: "))
    return par

def cercaOrizzontale(trov,pi,pj,mat,mat2,N,M,parola):  
    frase=""
    for i in range(N):
        if(trov==True):
            break
        for j in range(M-len(parola)+1):
            for k in range(len(parola)):
                if(mat[i][j+k]!=parola[k]):
                    break
                else:
                    frase+=mat[i][j+k]
                if(frase==parola):
                    trov=True
                    pi=i
                    pj=j
                    mat2=cancellaOrizzontale(mat2,mat,pi,pj,parola)
                
    return trov , pi , pj , mat2

def cercaVerticale(trov,pi,pj,mat,mat2,N,M,parola):
    frase=""
    for j in range(M-len(parola)+1):
        if(trov==True):
            break
        for i in range(N):
            for k in range(len(parola)):
                if(mat[j+k][i]!=parola[k]):
                    break
                else:
                    frase+=mat[j+k][i]
                if(frase==parola):
                    trov=True
                    pi=j
                    pj=i
                    mat2=cancellaVerticale(mat2,mat,pi,pj,parola)
                
    return trov , pi , pj , mat2

def cercaDiagonale(trov,pi,pj,mat,mat2,N,M,parola):
    frase=""
    l1=False
    for j in range(M-len(parola)+1):
        if(trov==True):
            break
        for i in range(N-len(parola)+1):
            for k in range(len(parola)):
                if(mat[i+k][j]!=parola[k] and l1==False):
                    break
                else:
                    l1=True
                    pi=i
                    pj=j
                    frase+=mat[i+k][j+k]
            if(frase==parola):
                trov=True
                mat2=cancellaDiagonale(mat2,mat,pi,pj,parola)
            l1=False
    return trov , pi , pj , mat2

def scrivi_parola_nascosta(mat2,mat,N,M):
    st=""
    i=j=0
    for i in range(N):
        for j in range(M):
            if(mat2[i][j]==1):
                st+=mat[i][j]

    return st                
  
def cancellaOrizzontale(mat2,mat,pi,pj,parola):
    for j in range(len(parola)):
        if(mat2[pi][pj+j]!=0):
            mat2[pi][pj+j]=0
    return mat2

def cancellaVerticale(mat2,mat,pi,pj,parola):
    for j in range(len(parola)):
        if(mat2[pi+j][pj]!=0):
            mat2[pi+j][pj]=0
    return mat2
    
def cancellaDiagonale(mat2,mat,pi,pj,parola):
    for i in range(len(parola)):
        if(mat2[pi+i][pj+i]!=0):
            mat2[pi+i][pj+i]=0
    return mat2
    
def main():
    N=int(input("N: "))
    M=int(input("M: "))
    mat=[]
    mat=cream(N,M,mat)
    parola=""
    mat2=[]
    mat2=cream2(mat2,N,M)
    trov=False
    K=int(input("K: "))
    par=[]
    par=creap(par,K)
    pi=pj=0
    for cont in range(K):
        parola=par[cont]
        if(trov==False):
            trov , pi , pj , mat2 = cercaOrizzontale(trov,pi,pj,mat,mat2,N,M,parola)
        if(trov==False):
            trov , pi , pj , mat2 = cercaVerticale(trov,pi,pj,mat,mat2,N,M,parola)
        if(trov==False):
            trov , pi , pj , mat2 = cercaDiagonale(trov,pi,pj,mat,mat2,N,M,parola)
        trov=False
        parola=""
    print(scrivi_parola_nascosta(mat2,mat,N,M),sep="",end="")
main()