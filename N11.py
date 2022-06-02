N=int(input())
N_New=str(N)
if "0" in N_New:
    print("NO")
elif N_New[:1]!=0:
    print("SI")