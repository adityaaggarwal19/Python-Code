def successor(n):
    '''
    Objective: To find the successor of the given non negative number n
    Input Parameter:
        n: A non negative integer of which the successor to be find out
    Output:
        Successor of the given non negative number n
    '''
    #Approach: Successor of n= n +1
    #assert n>=0
    if n<0:
        print("Error ",n, " < 0")
        return
    return n+1
def predecessor(n,m=0):
    '''
    OBJECTIVE: To find the predecessor of the given natural number n using comparison and successor function
    INPUT PARAMETER:
        n: A natural number of which the predecessor to be find out
        m: a candidate for finding the predecessor (taken as default parameter with value 0)
    OUTPUT:
        Predecessor of the natural number n
    '''
    #Approach: If successor(X)==n, then Predecessor(n)=X where 0<=X<n
    if n<1:
        return "Not a Natural Number" 
    if successor(m)==n:
        return m
    return predecessor(n,successor(m))
def add(m,n):
    '''
    OBJECTIVE: To perform the addition of two non-negative numbers.
    INPUT PARAMETERs:
            m: First number.
            n: Second number.
    OUTPUT: Return the sum of the two numbers.
    '''
    #APPROACH:Using succ(n) and pred(n) to add numbers.

    if n==0:
        return m
    else:
        return add(successor(m),predecessor(n))