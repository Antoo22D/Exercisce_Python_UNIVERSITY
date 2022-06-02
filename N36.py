sol = True
l = []

for i in range(10):
    n = l.append(int(input()))
x = int(input())
for j in l:
    if j%x == 0:
        sol = False

if sol:
    print("OK",end="")
else:
    print("NO",end="")