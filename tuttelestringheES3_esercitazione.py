def genera(C,I,k):
    if k==len(I):
        return
    for i in range(len(C)):
        for j in range(len(C)):
            if i !=j:
                print(str(I[k])+C[i]+C[j])
    genera(C, I, k+1)
def genera2(C,I,k,i,j):
    if k==len(I):
        return
    if i==len(C):
        genera2(C, I, k+1, 0, 0)
    elif j==len(C):
        genera2(C, I, k, i+1, 0)
    else:
        if i!=j:
            print(str(I[k])+C[i]+C[j])
        genera2(C, I, k, i, j+1)

C=["a","*","w"]
I=[1,13]
genera2(C, I, 0, 0, 0)