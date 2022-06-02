n=4
sum=0
mat=[[1,0,3,4],[0,-2,5,9],[28,0,0,1],[12,1,5,81]]
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i+j==(n-1):
            sum=sum+mat[i][j]
            print(sum)