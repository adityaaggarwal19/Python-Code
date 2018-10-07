def insertList(list1, el, i=0):
    '''
    OBJECTIVE:- To insert an element in non decreasing list at respective position
    INPUT:-
        list1: Sorted list elements is given to us
        el: element to be inserted in lst
        i: Default parameter for refering the index of the list
    OUTPUT:- Return a list with element inserted at respective position
    '''
    #Approach: Use recursion to find the respective position in the list i.e. insertlist(list1,el,i=1)
    if i == len(list1):
        list1.insert(idx, el)
        return lst
    elif el <= list1[i]:
        list1.insert(i, el)
        return list1 
    else:
        return insertList(list1, el, i+1)