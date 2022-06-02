#def elimina(l,i,booleana):
    nuoval=[]
    if i==len(l)-1:
        nuoval.append(l[i])
    else:
        if l[i]!=l[i+1]:
            nuoval.append(l[i])
    for j in range(1,len(nuoval)-2,2):
        if nuoval[j]>=nuoval[j+2]:
            booleana=False
    return booleana
#def main():
    # seq=int(input())
    # l=[]
    # booleana=True
    # for i in range(len(l)-1):
    #     l.append(seq)
    # while seq!=".":
    #     seq=input()
    #     l.append(seq)
    # print(elimina(l, 0, booleana))
#main()

seq=input()
l=[]
bule= True
while seq!=".":
    l.append(seq)
    seq=input()
nuovaL=[]
for i in range(len(l)):
    if i==(len(l)-1):
        nuovaL.append(l[i])
    else:
        if l[i]!=l[i+1]:
            nuovaL.append(l[i])
for j in range(1,len(nuovaL)-2,2):
    if nuovaL[j]>=nuovaL[j+2]:
        bule=False
if bule:
    print("SI")
else:
    print("NO")
