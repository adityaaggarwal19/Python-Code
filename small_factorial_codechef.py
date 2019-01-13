def fact(k):
    if k==1:
        return 1
    else:
        return k*fact(k-1)
t=int(input())
while t>0:
	k=int(input())
	print(fact(k))
	t=t-1
