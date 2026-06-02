n=int(input())
t=n
s=0
count=0
while n>0:
    n=n//10
    count+=1
print(count)
while t>0:
    r=t%10
    s=s+r**count
    t=t//10
    count-=1
print(s)
