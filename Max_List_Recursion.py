'''
OBJECTIVE:- To find the maximum element in the list
'''
def maxi(l):
    if len(l)==1:
        return l[0]
    else:
        ma=maxi(l[0:len(l)-1])
        if l[len(l)-1]<ma:
            return ma
        else:
            return l[len(l)-1]
maxi([10,5,3])