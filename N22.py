seq=""
err=0
stop="a"

while stop!=".":
    n=str(input())
    if n!=".":
        seq+=n
    else:
        stop="."
for i in seq:
    if i.isalpha()==True:
        err+=1
if err>0:
    print("SI",end="")
else:
    print("NO",end="")
    