stop = "a"
seq = ""
err = 0

while stop != ".":
    n = str(input())
    if n != ".":
        seq += n
    else:
        stop = "."

for i in seq:
    if i.isalpha() == False:
        err += 1

if err > 0:
    print("NO", end="")
else:
    print("SI", end="")
