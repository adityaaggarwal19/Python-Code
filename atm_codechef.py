n=input()
l=list(n.split(" "))
a=int(l[0])
b=float(l[1])
if (a+0.50)>b:
    print('%.2f'%b)
else:
    if a%5==0:
        b=b-a-0.50
        print('%.2f'%b)
    else:
        print('%.2f'%b)
