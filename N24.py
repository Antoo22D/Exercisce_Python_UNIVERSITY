def sottoseq(stringa,somma):
    vocali="aeiou"
    if len(stringa)==0:
        return 0
    for i in range(len(stringa)-1):
        if (stringa[i]in vocali and stringa[i+1] in vocali) or (stringa[i]not in vocali and stringa[i+1]not in vocali):
            somma+=1
    return somma
def main():
    n=input()
    stringa=""
    while n!=".":
        stringa+=n
        n=input()
    print(sottoseq(stringa, 1))
main()

