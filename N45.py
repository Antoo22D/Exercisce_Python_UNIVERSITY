def risultato(n,n2,nmax,nmin):
    if n==0:
        print("0")
    for i in str(n):
        n2.append(i)
    n2.sort()
    
    for i in n2:
        nmin+=str(i)
    n2.reverse()
    
    for j in n2:
        nmax+=str(j)
    ris=0
    ris=int(nmax)-int(nmin)
    return ris
def main():
    n=int(input())
    n2=[]
    nmax=""
    nmin=""
    totale=risultato(n,n2,nmax, nmin)
    print(totale)
main()