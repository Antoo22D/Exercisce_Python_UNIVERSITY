n=int(input())
numeri=[1]
for i in range(n-1):
    numeri.append(numeri[i]+2)
print(sum(numeri)*2-numeri.pop(),end="")