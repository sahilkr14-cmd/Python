# You are given an array prices[], in which each element is the stock price on a particular day.
# You can buy stock once and sell it once.
# You have to extract maximum profit.


def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    
    return max_profit

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([2, 4, 1]))