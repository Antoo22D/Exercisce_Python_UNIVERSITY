stop = "a"
seq = ""
num = 0
while stop != "*":
    n = str(input())
    if n != "*":
        seq += n
    else:
        stop = "*"

for i in seq:
    if i.isdigit() == True:
        num += 1

if num > 0:
    print("ALMENO UNA", end="")
else:
    print("NESSUNA", end="")