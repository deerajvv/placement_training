def fun(n):
    if n==18:
        print(16)
        return
    print(n-8)
    fun(n+2)

n=10
fun(n)