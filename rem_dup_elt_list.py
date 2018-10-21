lis=[]
n= int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    elt=int(input("Enter the element in the list" + str(i+1) + " :"))
    lis.append(elt)
lis1 = set()
unique = []
for i in lis:
    if i not in lis1:
        unique.append(i)
        lis1.add(i)
print("Non-duplicate items are:")
print(unique)