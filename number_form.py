n=int(input("Enter a number= "))
tmp=n
k=0
while(n>0):
    k=k+1
    n=n//10
b=str(tmp)
c=str(k)
d=c+b[k-1]
print("Number formed= ",int(d))