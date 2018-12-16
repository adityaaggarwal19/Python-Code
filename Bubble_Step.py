def bubbleStep(lst,index,i=-1,j=-1):
    if j==index:
        return lst
    else:
        if i==-1:
            i=len(lst)-1
            j=i-1
        if lst[i]<lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
        return bubbleStep(lst,index,i-1,j-1)
print(bubbleStep([1,2,3,4,7,6,5],3))
