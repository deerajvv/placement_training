n,m,a,b=map(int,input().split())
sum=0
if a*m<b:
    sum=sum+n*a
else:
    print(((n//m)*b)+min(b,(n%m)*a))
print(sum)

