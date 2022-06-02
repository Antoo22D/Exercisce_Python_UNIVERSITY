def corretta(funzione,miafun):
    for i in range(len(miafun)):
        if miafun[i]!="def":
            return False
        else:
            if miafun[i+1] and miafun[i+2]=="(" and miafun[len(miafun[i-2])]==")":
                if miafun[i+3].isidentifier() and miafun[i+4]==",":
                    return miafun
                    return True
            return miafun
def main():
    funzione=input()
    miafun=[]
    while funzione!=":":
        miafun.append(funzione)
        funzione=input()
    if corretta(funzione, miafun):
        print("SI")
    else:
        print("NO")
main()
