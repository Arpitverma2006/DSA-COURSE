def maxProfit(prices):   #Hard Level Program
    min_price_after_first_buy=float('inf')
    max_profit_after_first_sell=0
    min_price_after_second_buy=float('inf')
    max_profit_after_second_sell=0

    for price in prices:
        min_price_after_first_buy=min(min_price_after_first_buy,price)
        max_profit_after_first_sell=max(max_profit_after_first_sell,price-min_price_after_first_buy)
        min_price_after_second_buy=min(min_price_after_second_buy,price-max_profit_after_first_sell)
        max_profit_after_second_sell=max(max_profit_after_second_sell,price-min_price_after_second_buy)
    return max_profit_after_second_sell


prices=[3,3,5,0,0,3,1,4]
res=maxProfit(prices)
print(res)

