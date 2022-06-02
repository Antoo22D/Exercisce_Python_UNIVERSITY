n=int(input())
a=[]
somma=0
sommaesterna=0
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(int(input()))
for i in range(n):
    for j in range(n):
        if n//2==j or n//2==i:
            somma+=a[i][j]
        else:
            sommaesterna+=a[i][j]
if somma>sommaesterna:
    print("SI")
else:
    print("NO")
