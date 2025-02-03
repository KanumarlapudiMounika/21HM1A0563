def primenum(s):
    n='2357'
    s1=''
    s2=0
    for i in s:
        if i in n:
            s1=s1+i
            s2=s2+int(i)
    if s2!=0:
        print(s1,':',s2)
    else:
        print(s[0],':',s[(len(s))-1])
s=input()
primenum(s)
