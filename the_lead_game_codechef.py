n=int(input())
ma=0
po=0
a=0
b=0
while n>0:
    s=input()
    l=s.split(" ")
    a=a+int(l[0])
    b=b+int(l[1])
    if a>b:
        res=a-b
        if ma<res:
            ma=res
            po=1
    else:
        res=b-a
        if ma<res:
            ma=res
            po=2
    n=n-1
print(po," ",ma)

