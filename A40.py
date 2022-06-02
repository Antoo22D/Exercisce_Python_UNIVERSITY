l=[]
a=int(input())

while a!=-50:
    l.append(a)
    a=int(input())
if len(l)!=0:
    media=sum(l)//len(l)
    
    
    sotts=[]
    for i in range(0,len(l)):
        if l[i]>=media:
            sotts.append(l[i])
    print(min(sotts),end="",sep="")
else:
        print("VUOTA",end="",sep="")
        
        
