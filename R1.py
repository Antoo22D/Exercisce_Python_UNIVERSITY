def ricorsione1(N):
    if N==0:
        return 2
    if N>0:
        return 3*(N+1)*ricorsione1(N-1)
    return ricorsione1
def main():
    N=int(input())
    print(ricorsione1(N),end="")
main()