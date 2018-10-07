def insertSList(value, list1, i=0):
    '''
    OBJECTIVE:- To insert an element in a sorted list such that the list remains sorted.
    INPUT:-
        value: Given Value to be inserted in the sorted list
        list1  : Given sorted list of elements in which the element to be inserted
        i: Default parameter whose value is 0 initially
    OUTPUT:- Return the list with inserted value
    '''
    #Approach: Use Recursion to insert the element when the element at a position is greater than the element then we insert the element.
    if list1==[]:
        list1.insert(0, value)
    elif list1[i:]==[]:         
        list1.append(value)    
    elif list1[i]>value:
        list1.insert(i,value)
    else:
        insertSList(value, list1, i+1)

def mergeList(list1,list2,i=0):
    '''
    OBJECTIVE:- To insert elements of one list 2 into another list 1 such that list 1
    INPUT:
        list1: Given sorted list of values
        list2: A list of values which need to be merged
        i : Default Parameter with value = 0
    OUTPUT:- Returns the merged sorted list
    '''
    #Approach: Recursively inserting by using function insertSList()
    if list2[i:]==[]:
        return
    else:
        insertSList(list2[i],list1)
        mergeList(list1,list2,i+1)