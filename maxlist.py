def maximum(a,b):
    '''
    OBJECTIVE:- To find the larger number of the two numbers.
    INPUT:-
        a:  1st number 
        b:- 2nd number
    OUTPUT: Returns the larger number of the two numbers.
    '''
    #Approach: Compare the two numbers by using if statement. i.e. a>=b then return a else b

    if a>=b:
        return a
    return b

def maxlist(list1):
    '''
    OBJECTIVE:- To find the largest number in the list.
    INPUT:-
        list1:- Input of List of numbers.
    OUTPUT:- Returns the largest number from the list.
    '''
    #Approach: Recursive use of maximum(a,b) function to compare two elements of the list and recusrsively check for rest

    if len(list1)==0:
        return "List is empty"
    if len(list1)==1:
        return list1[0]
    else:
        return maximum(list1[0],maxlist(list1[1:]))