s="aaaaabbbbcccc"
res=""
count=1
k=0
for i in range(1,len(s)):
    if s[k]==s[i]:
        count+=1
    else:
        res+=s[i-1]+str(count)
        k=i
        c=1
res+=s[-1]+str(c)
print(res)








