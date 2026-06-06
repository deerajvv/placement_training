s=str(input())
count=0
count1=0
count2=0
count3=0
count5=0
space=False
for i in range(len(s)):
    if s[i].isupper()==True:
        count1+=1
    if s[i].islower()==True:
        count5+=1
    if s[i].isalpha()==True:
            count+=1
    if s[i]==" ":
        space=True
    if s[i].isdigit()==True:
            count2+=1
    if s[i] in "@#$%^&*_":
            count3+=1
if len(s)>=8 and count!=0 and count2!=0 and count3!=0 and count1!=0 and count5!=0 and space==False:
    print("password success")
else:
    print("password fail")

