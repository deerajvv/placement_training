n=list(map(int,input().split()))
key=int(input())
l=len(n)-1
s=0
m=s+l//2
while s!=l:
    if n[m]==key:
        print("found")
    elif key<n[m]:
        l=m-1
        m = s + l // 2
    elif key>n[m]:
        s=m+1
        m = s + l // 2

