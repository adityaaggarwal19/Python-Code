def cum_lst(lst,cumlst=[],i=0):
    if i==len(lst):
        return cumlst
    else:
        a=sum(lst[:i+1])
        #print (a)
        cumlst.append(a)
        return cum_lst(lst,cumlst,i+1)
b=[1,2,3,4,5,6,7,8,9,10]
print(cum_lst(b))
