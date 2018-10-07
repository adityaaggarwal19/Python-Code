def prime(n):
    '''
    OBJECTIVE:- To find whether a given number is prime or not
    Input:- A given number n
    Output:- Whether the number is prime or not
    '''
    #Approach: Find N%i and if remainder is 0 then number is divisible and not a prime number. i will range till sqrt(n)
    if n<=1:                #Since prime number start from 2 as 2 is the smallest prime number 
        return False
    i=2                    #Initializing loop parameter i with the value 2
    while i*i<=n:          # loop will run until i is sqrt(n)
        if n%i==0:         #checking for divisibility of n by i
            return False   #returning false if number is divisible
        i+=1               
    return True            #if the number is not divisible by any number till sqrt(n) then return true