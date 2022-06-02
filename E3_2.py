def sottos(miaseq1,sottoseq):
    sotss=[]
    for i in range(len(miaseq1)):
        if i ==len(miaseq1)-1:
            sotss.append(miaseq1[i])
            if len(sotss)>=2:
                sottoseq+=1
        else:
            if int(miaseq1[i])+1==int(miaseq1[i+1]):
                sotss.append(miaseq1[i])
            else:
                sotss.append(miaseq1[i])
                if len(sotss)>=2:
                    sottoseq+=1
                sotss=[]
    return sottoseq
def main():
    seq=input()
    miaseq=[]
    sottoseq=0
    while seq!="*":
        miaseq.append(seq)
        seq=input()
    print(sottos(miaseq, sottoseq),end="")
main()
