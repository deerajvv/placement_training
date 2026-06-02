l1=input().split()
l2=[]
for i in l1:
    if i not in l2 and l1.count(i)%2!=0:
        l2.append(i)
print(l2)