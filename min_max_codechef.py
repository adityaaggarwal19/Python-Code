t=int(input())
while t>0:
    n=int(input())
    s=input()
    cost=0
    l=s.split(" ")
    for i in range(0,n):
        l[i]=int(l[i])
    l=list(set(l))
    while len(l)!=1:
        if l[0]<l[1]:
            cost=cost+l[0]
            l.remove(l[1])
        else:
            cost=cost+l[1]
            l.remove(l[0])
    print(cost)
    t=t-1
'''
    for i in range(0,len(l)-1):
        if i>=len(l)-1:
            break
        if l[i]<l[i+1]:
            l.remove(l[i+1])
            cost=l[i]
        else:
            cost=l[i+1]
            l.remove(l[i])

    while len(l)!=1:
        if l[0]<l[1]:
            cost=l[i]
            l.remove(l[i+1])
        else:
            cost=l[i+1]
            l.remove(l[i])
    print(cost)
    t=t-1
'''
