l=list(map(int,input().split()))
l2=[]
l.sort()
for i in l:
    if i%2!=0:
        l2.append(i)
    else:
        l2.insert(0,i)
print(l2)
