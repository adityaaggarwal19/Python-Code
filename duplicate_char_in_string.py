def dup_char(s):
    l=[]
    l=set(l)
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            l.add(s[i])
    l=list(l)
    for i in range(0,len(l)):
        print(l[i],end=" ")
dup_char("aabbccdddee")
