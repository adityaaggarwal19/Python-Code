    arr=[[11,2,4],[4,5,6],[10,8,-12]]
    sum_l_r=0
    sum_r_l=0
    for i in range(0,len(arr[0])):
        sum_l_r=sum_l_r+arr[i][i]
    i=0
    j=len(arr[0])-1
    while i<len(arr[0]) and j>=0:
        sum_r_l=sum_r_l+arr[i][j]
        i=i+1
        j=j-1
    res=abs(sum_l_r-sum_r_l)
    print(res)