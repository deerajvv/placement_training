lis=list(map(int,input().split()))
k=int(input())
j=0
m=0
for i in range(j,k+1):
    sum+=lis[i]
    if sum>m:
        m=sum
    j+=1

print(m)
