def fun(n,count):
    if n==1:
        print(count)
        return
    elif n%2==0:
        count += 1
        fun(n//2,count)

    elif n%2!=0:
        if ((n+1)//2)%2==0:

            count += 1
            fun(n+1,count)
        elif ((n-1)//2)%2==0:
            count+=1
            fun(n - 1, count)




n=int(input())
count=0
fun(n,count)

