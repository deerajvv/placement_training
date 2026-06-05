list=list(map(int,input().split()))
n=int(input())
for i in range(n):
    temp=list[0]
    for i in range(1,len(list)):
        list[i-1]=list[i]
    list[-1]=temp
print(list)