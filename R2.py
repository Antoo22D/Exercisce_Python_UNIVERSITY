def ricorsione2(l,j):
    if len(l)%2!=0:
        return False
    else:
        if j<len(l)//2:
            if l[j]==l[(len(l)//2)+j]:
                return ricorsione2(l, j+1)
            else:
                return False
        return True
def main():
    N=int(input())
    l=[]
    for i in range(N):
        l.append(int(input()))
    if ricorsione2(l, 0):
        print("SI")
    else:
        print("NO")
main()
