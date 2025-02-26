def climbStairs(n):
    if n<=3:
        return n
    p1=3
    p2=2
    c=0

    for i in range(3,n):
        c=p1+p2
        p2,p1=p1,c

    return c


n=int(input("Enter the number of Stairs : "))
r=climbStairs(n)
print(r)

