n=int(input())
migliaia=["M"]
centinaia=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
decine=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
unita=["","I","II","III","IV","V","VI","VII","VIII","IX"]
converto=str(n)
numRom=""
if len(converto)==1:
    numRom+=unita[int(converto)]
elif len(converto)==2:
    numRom+=decine[int(converto[0])]+unita[int(converto[1])]
elif len(converto)==3:
    numRom+=centinaia[int(converto[0])]+decine[int(converto[1])]+unita[int(converto[2])]
elif len(converto)==4:
    numRom+=migliaia[0]+centinaia[int(converto[1])]+decine[int(converto[2])]+unita[int(converto[3])]
print(numRom)


