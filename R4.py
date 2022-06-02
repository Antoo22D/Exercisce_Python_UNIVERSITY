def ricorsiva(N, x, somma, occ):
    if N.count(x) == 0:
        return somma
    elif N.count(x) == 1 and occ != 0:
        N[N.index(x)] = 0
        c = occ
        occ = 0
        return ricorsiva(N, c, somma, occ)
    elif N.count(x) == 1 and occ == 0:
        N[N.index(x)] = 0
        occ == 1
        somma += occ
        return ricorsiva(N, occ, somma, occ)
    elif occ == 0:
        occ = N.count(x)
        somma += occ
        return ricorsiva(N, x, somma, occ)
    elif occ != 0:
        N[N.index(x)] = 0
        return ricorsiva(N, x, somma, occ)

def main():
    x = int(input())
    n = int(input())
    N = []
    for i in range(n):
        N.append(int(input()))
    print(ricorsiva(N, x, 0, 0), end="")
main()