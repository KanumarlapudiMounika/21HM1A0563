a=input()
c=1
b=[int(i) for i in a]
for j in range(0,len(b)):
    if b[j] < b[-1]:
        a=c*b[j]
        c=c+1
        b.pop(j)
        print('beg',a)
        print(b)
    else:
        a=c*b[-1]
        c=c+1
        b.pop()
        print('end',a)
        print(b)
        
        
