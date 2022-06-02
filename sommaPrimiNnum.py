def main():
    n=int(input())
    print(sommanpriminumeri(n))
def sommanpriminumeri(n):
    num=int(input("Valore di n: "))
    somma = 0
    for i in range(1,n+1):
        somma += i
    print('La somma dei primi ' + str(n) + ' numeri vale ' + str(somma))
    sommanpriminumeri(num)
main()