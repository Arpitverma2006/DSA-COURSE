def maxProfit(k,prices):
    if k==0:
        return 0

    dp=[[1000,0] for _ in range(k+1)]

    for price in prices:
        for i in range(1,k+1):
            dp[i][0]=min(dp[i][0],price-dp[i-1][1])
            dp[i][1]=max(dp[i][1],price-dp[i][0])

    return dp[k][1]


prices=[2,4,1]
k=2
res=maxProfit(k,prices)
print(res)


