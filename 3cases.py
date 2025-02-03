n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)

msum=0
c=0
mc=0
sum1=0
for i in range(n):
    if a[i]>0:
        sum1=sum1+a[i]
        c=c+1 
    else:
        if c>mc:
            mc=c 
            msum=sum1
        elif c==mc:
            msum=msum+sum1
        c=0
        sum1=0
if c==mc:
    msum=msum+sum1
if msum!=0:
    print(msum)
else:
    print('-1')
    
