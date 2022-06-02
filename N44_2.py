def decifra(A,B,i,x):
    parola=""
    for x in range(len(B)):
        if B[x]>=0 and B[x]<26:
            parola+=str(A[B[x]])
            
    return parola

def main():
    A=[]
    for i in range(26):
        A.append(input())
    N=int(input())
    B=[]
    for x in range(N):
        B.append(int(input()))
    print(decifra(A, B, i, x),end="")
main()