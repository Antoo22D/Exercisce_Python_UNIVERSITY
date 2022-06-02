def controlla(lista,n):
    vero=0
    if len(lista)==0:
        print("NO")
    for i in range(len(lista)):
        if lista[i]<=n:
            vero+=0
        else:
            vero+=1
    if vero>0:
        print("OK")
    else:
        print("NO")
def main():
    n=int(input())
    lista=[]
    while n>0:
        lista.append(n)
        n=int(input())
    print(controlla(lista, n))
main()