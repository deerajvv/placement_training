list=list(map(int,input().split()))
d={}
max=0
secmax=0
ele=0
el2=0
for i in list:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
for i in d:
    if d[i]>max:
        secmax=max
        el2=ele
        max=d[i]
        ele=i


    elif d[i]<max and d[i]>secmax:
        secmax=d[i]
        el2=i
print(ele)
print(el2)