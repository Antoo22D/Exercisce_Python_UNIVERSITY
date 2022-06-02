def funzione(miaseq,seq):
    for i in range(len(miaseq)):
        if miaseq[i]!="def":
            return False
        else:
            if miaseq[i+1].isalpha() and miaseq[i+2]=="(" and miaseq[len(miaseq[i-2])]==")":
                if miaseq[i+3].isidentifier() and miaseq[i+4]==",":
                    return miaseq
                return True
            return miaseq
                
def main():
    seq=input()
    miaseq=[]
    while seq!=":":
        miaseq.append(seq)
        seq=input()
    if funzione(miaseq, seq):
        print("SI")
    else:
        print("NO")
main()