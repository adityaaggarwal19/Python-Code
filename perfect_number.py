def PerfectNumber( n ): 
      
    i = 2
    sum1 = 1
    for i in range(2, n//2):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The given number is a Perfect number because sum of its factor is equal to itself!")
    else:
        print("The given number is not a Perfect number!")
    
n = int(input("Enter a number for which we need to check for:- "))
PerfectNumber( n )
