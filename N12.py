def numPrim(N):
    cont=0
    for i in range(1,N+1):
        if N%i==0:
            cont+=1
    if cont>2:
        return True
    else:
        return False
def main():
    N=int(input())
    if numPrim(N):
        print("NO",end="")
    else:
        print("SI",end="")
main()