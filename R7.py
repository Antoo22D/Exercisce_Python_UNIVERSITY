def main():
    A=int(input())
    B=int(input())
    print(mcd(A, B),end="")    
def mcd(A,B):
    if A==0 or B==0:
        return 0
    r=A%B
    if r==0:
        return B
    else:
        A=B
        B=r
        return mcd(A,B)
main()