def fun(n):
    if n==0:
        return
    if n%2==0:
        print(n)
    fun(n-1)
    if n%2==0 and n>3:
        print(n)

n=10
fun(n)