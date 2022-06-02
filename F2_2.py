def creap(par):
    s=input()
    while(s!="."):
        par+=s
        s=input()
    return par
def pari(par,alf,n2,pos,st,i):
    pos=alf.index(par[i])
    for i in range(n2):
        if(pos==0):
            pos=len(alf)-1
        else:
            pos-=1
    st+=alf[pos]
    return st
def dispari(par,alf,n1,pos,st,i):
    pos=alf.index(par[i])
    for i in range(n1):
        if(pos==len(alf)-1):
            pos=0
        else:
            pos+=1
    st+=alf[pos]
    return st
def parola_cifrata(par,n1,n2):
    alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pos=0
    st=""
    for i in range(len(par)):
        if((i+1)%2==0):
            st = pari(par,alf,n2,pos,st,i)
        else:
            st = dispari(par,alf,n1,pos,st,i)
    return st
def main():
    n1=int(input())
    n2=int(input())
    par=""
    par=creap(par)
    print(parola_cifrata(par,n1,n2),end="")
main()