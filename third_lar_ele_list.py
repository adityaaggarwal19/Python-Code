lis=[]
n=int(input("Enter the Number of Elements in the list: "))
for i in range(1,n+1):
    lis1=int(input("Enter element:"))
    lis.append(lis1)
for i in range(0,len(lis)):
    for j in range(0,len(lis)-i-1):
        if(lis[j]>lis[j+1]):
            temp=lis[j]
            lis[j]=lis[j+1]
            lis[j+1]=temp 
print('Third largest element is:',lis[n-3])