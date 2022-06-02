tappo = 1
seq = ""
sol = 0
N = 0
M = 0 
while tappo != 0:
    x = int(input())
    if x == 0:
        tappo = 0
    else:
        if N == 0:
            N = x
        elif M == 0:
            M = x
            if (N%2 == 0 and M%2 == 0) or (N+M)%N == 0 or (N+M)%M == 0:
                sol += 1
        else:
            N = M
            M = x
            if (N%2 == 0 and M%2 == 0) or (N+M)%N == 0 or (N+M)%M == 0:
                sol += 1
if sol > 0:
    print("SI", end="")
else:
    print("NO", end="")