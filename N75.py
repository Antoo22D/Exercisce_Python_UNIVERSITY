frase=input()
pangramma=True
tutto=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in tutto:
    if frase.count(i)==0:
        pangramma=False
if pangramma:
    print("SI")
else:
    print("NO")