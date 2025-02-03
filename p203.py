def add(e):
    sum=sum+e
n=int(input())
a=list(map(int,input().split()))
a.sort()
print(a.sort())
b=add(a[1:n-1])
c=a[0]+a[n]
print(b-c)
