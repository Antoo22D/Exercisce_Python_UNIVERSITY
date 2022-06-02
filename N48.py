'''def controllo(n,seq,numPrec,cresc,sup):
    for i in range(1,len(seq)):
        if seq[i-1]<=seq[i+1]:
            numPrec.append(seq[i-1])
            if i==len(seq)-1:
                numPrec.append(seq[i])
                if len(numPrec)>len(cresc):
                    cresc=list(numPrec)
                    numPrec=[]
        else:
            numPrec.append(seq[i-1])
            if len(numPrec)>len(cresc):
                cresc=list(numPrec)
                numPrec=[]
            else:
                numPrec=[]
    for j in cresc:
        sup+=str(j)
    print(cresc)
    print(len(cresc))
def main():
    n=int(input())
    seq=[]
    numPrec=[]
    cresc=[]
    sup=""
    contr=controllo(n, seq, numPrec, cresc, sup)
    if n<0:
        print("Empty",end="")
    while n>=0:
        seq.append(n)
        n=int(input())
    print(contr)
main()
'''

seq=[]
n=int(input())
numPrec=[]
cresc=[]
sup=""

if n<0:
    print("Empty",end="")
else:
    while n >=0:
        seq.append(n)
        n=int(input())
    for i in range(1,len(seq)):
        if seq[i-1]<=seq[i]:
            numPrec.append(seq[i-1])
            if i==len(seq)-1:
                numPrec.append(seq[i])
                if len(numPrec)>len(cresc):
                    cresc=list(numPrec)
                    numPrec=[]
        else:
            numPrec.append(seq[i-1])
            if len(numPrec)>len(cresc):
                cresc=list(numPrec)
                numPrec=[]
            else:
                numPrec=[]
    for j in cresc:
        sup+=str(j)
    print(sup)
    print(len(cresc),end="")
    