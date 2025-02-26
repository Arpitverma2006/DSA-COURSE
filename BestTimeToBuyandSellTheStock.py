#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
def maxProfit(self,prices): # This is a brute force technique .
    b_p=prices[0]
    profit=0
    for i in prices[1:]:
        if b_p>i:
            b_p=i
        profit=max(profit,i-b_p)
    return profit

prices=[7,1,5,3,6,4]
res=maxProfit(None,prices)
print(res)


