def eno_inp_test(n,k):
    if n%k==0:
        return 1
    else:
        return 0
if __name__=="__main__":
    count=0
    n=int(input())
    k=int(input())
    while n>0:
        t=int(input())
        count=count + eno_inp_test(t,k)
        n=n-1
    print(count)
