seq=input()
stop="a"
err=0

while stop != "*":
    n = str(input())
    if n != "*":
        seq += n
    else:
        stop = "*"

for i in seq:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        err += 1

if err > 0:
    print("ALMENO 1 VOCALE", end="")
else:
    print("NESSUNA VOCALE", end="")