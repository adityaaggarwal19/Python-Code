'''
OBJECTIVE:- To find the maximum element in the list
'''
def maxi(l,n):
    if (n == 1): 
        return l[0] 
    return max(l[n - 1], maxi(l, n - 1)) 
l=[10,5,3] 
n = len(l) 
maxi(l,n)
