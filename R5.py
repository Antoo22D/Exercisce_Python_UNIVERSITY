'''def inverso(l,i):
    if i<0:
        return str()
    return l[::-1]
def main():
    n=int(input())
    l=[]
    for _ in range(n):
        l.append(int(input()))
    print(inverso(l, 0))
main()
'''

def ricorsione(N,i):
    if i < 0:
        return str()
    return str(N[i])+ricorsione(N, i-1)
def main():
    n=int(input())
    N=[]
    for j in range(n):
        N.append(int(input()))
    print(ricorsione(N,len(N)-1),end="")
main()