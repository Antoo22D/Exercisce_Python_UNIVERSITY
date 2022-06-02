def main():
    n = int(input())
    N = []
    N = matriceRicorsiva(N, n, 0)
    N = riempiMatRic(N, 0, 0)
    if controlloRic(N, 0, len(N)-1):
        print("SI", end="")
    else:
        print("NO", end="")
def matriceRicorsiva(N, n, i):
    if i >= n:
        return N
    N.append([0]*n)
    return matriceRicorsiva(N, n, i+1)
def riempiMatRic(N, i, j):
    if i >= len(N) and j == 0:
        return N
    elif i < len(N) and j < len(N[i]):
        N[i][j] = int(input())
        return riempiMatRic(N, i, j+1)
    elif j >= len(N[i]):
        return riempiMatRic(N, i+1, 0) 
def controlloRic(N, i, j):
    if i >= len(N) and j < 0:
        return True
    elle = 0
    for k in range(i,len(N)):
        elle += N[j][k]
    for k in range(j+1):
        elle += N[k][i]
    if elle % N[j][i] == 0:
        return controlloRic(N, i+1, j-1)
    else:
        return False
main()