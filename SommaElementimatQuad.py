def somma_ricorsiva(M,i):
    if i>=len(M):
        return 0
    somma=0
    for j in range(len(M)):
        somma+=M[i][j]
    return somma+somma_ricorsiva(M, i+1)
def main():
    M=[[1,2,5, 3],[0,2,0,2],[0,2,3,2],[1,2,3,4]]
    print(somma_ricorsiva(M, 0))
main()