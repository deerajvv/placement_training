def fun(n,m=0):
    if n==m:
        return
    print(m+1)
    fun(n,m+1)
    print(m+1)


n=5
fun(n)