list=input().split()
l=len(list)
temp=0
c=l//2-1
for i in range(0,l//4):
    temp=list[i]
    list[i]=list[c]
    list[c]=temp
    c-=1
print(list)