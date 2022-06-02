m=input()
cont=0

if m[0].isspace() or m[0].isnumeric():
    print("NO")
else:
    for i in range(1,len(m)):
        if m[1].isalnum() or m[i]=="_":
            continue
        else:
            print("NO")
            cont+=1
            break
    if cont==0:
        print("SI")