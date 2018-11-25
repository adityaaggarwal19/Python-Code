from collections import Counter
def sum_freq():
    
    t=int(input())
    while t>0:
        list_of_integers = []
        n=int(input())
        list_of_integers = list(map(int, input().split()))
        cnt = Counter(list_of_integers)
        b=cnt.values()
        d=min(b)
        a=cnt.most_common(1)
        c=a[0][1]
        print(d+c)
        t=t-1
sum_freq()
