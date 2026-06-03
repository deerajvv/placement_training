n=list(map(int,input().split()))
max=0
secmax=0
for i in n:
    if i>max:
        secmax=max
        max=i
    elif i<max and i>secmax:
        secmax=i
print(secmax)


