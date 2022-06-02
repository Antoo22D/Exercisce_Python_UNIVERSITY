'''def soddisfa(N,miaseq,seq):
    cont1=0
    cont=0
    if cont>=N:
        cont1+=1
        cont=0
    if seq<=N:
        cont+=1
    else:
        if cont>=N:
            cont1+=1
            cont=0
        else:
            cont=0
    if cont1!=0:
        return True
    else:
        return False
def main():
    N=int(input())
    seq=int(input())
    miaseq=[]
    while seq != -1:
        miaseq.append(seq)
        seq=int(input())
    if soddisfa(N, miaseq, seq):
        print("OK", end="")
    else:
        print("NO", end="")
main()'''

N = int(input())
cont = 0
tappo = 0
contF = 0
while tappo != -1:
    x = int(input())
    if x == -1:
        tappo = -1
        if cont >= N:
                contF += 1
                cont = 0
    else:
        if x <= N:
            cont += 1
        else:
            if cont >= N:
                contF += 1
                cont = 0
            else:
                cont = 0

if contF != 0:
    print("OK", end="")
else:
    print("NO", end="")