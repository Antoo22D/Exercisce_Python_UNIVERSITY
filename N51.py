seq1=input()
prima=[]
sec=[]
comune=""
while seq1!=".":
    prima.append(seq1)
    seq1=input()
z=input()
while z!=".":
    sec.append(z)
    z=input()

for i in prima:
    if i in sec:
        comune+=i
if len(comune)>=1:
    print(comune[0],end="")
else:
    print("DISGIUNTE")