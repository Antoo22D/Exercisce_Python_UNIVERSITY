def somme(A,somma,sommaesterna,n):
    for i in range(n):
        for j in range(n):
            if n//2==j or n//2==i:
                somma+=A[i][j]
            else:
                sommaesterna+=A[i][j]
    if somma>sommaesterna:
        return True
    else:
        return False
def creamat(n):
    A=[]
    for i in range(n):
        A.append([])
        for j in range(n):
            A[i].append(int(input()))
    return A
def main():
    n=int(input())
    A=creamat(n)
    sommaesterna=0
    somma=0
    if somme(A, somma, sommaesterna,n):
        print("OK",end="")
    else:
        print("NO",end="")
main()