'''
def prefix(l):
    return sum(l)
def suffix(l):
    return sum(l)
t=int(input())
while t>0:
    n=int(input())
    s=input()
    mi=999999999999999
    pos=0
    sump=0
    l=s.split(" ")
    for i in range(0,n):
        l[i]=int(l[i])
    for i in range(0,n):
        sump=sum(l[:i+1])+sum(l[i:n])
        if sump<mi:
            mi=sump
            pos=i
    print(pos+1)
    t=t-1
'''
def prefix(l):
    return sum(l)
def suffix(l):
    return sum(l)
t=int(input())
while t>0:
    n=int(input())
    mi=999999999999999
    pos=0
    sump=0
    l=[]
    for i in range(0,n):
        a=int(input())
        l.append(a)
    for i in range(0,n):
        sump=sum(l[:i+1])+sum(l[i:n])
        if sump<mi:
            mi=sump
            pos=i
    print(pos+1)
    t=t-1
