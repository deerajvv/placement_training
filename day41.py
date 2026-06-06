lis=[2,1,6,2,1,2,4,7,8,1,2]
k=10
r=0
l=0
m=0
s=0
while r<len(lis):

    s+=lis[r]
    while s>k:
        s-=lis[l]
        l+=1
    length=r-l+1
    m=max(m,length)
    r+=1
print(m)
