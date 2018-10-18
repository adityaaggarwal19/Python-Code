binary=[]
def convert(b):
    if(b==0):
        return binary
    dig=b%2
    binary.append(dig)
    convert(b//2)
a=int(input("Enter a number to convert into binary equivalent: "))
convert(a)
binary.reverse()
print("Binary equivalent:")
for i in l:
    print(i,end="")