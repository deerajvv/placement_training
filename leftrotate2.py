n=list(map(int,input().split()))
j=int(input())
l=len(n)
j=j%l
def rotate(i,j):
    while(i<j):
        n[i],n[j]=n[j],n[i]
        i+=1
        j-=1
rotate(0,j-1)
rotate(j,l-1)
rotate(0,l-1)
print(n)