t=int(input())
l=[]
while t>0:
    n=int(input())
    l.append(n)
    t=t-1
l=sorted(l)
for i in range(0,len(l)):
    print(l[i])

    
