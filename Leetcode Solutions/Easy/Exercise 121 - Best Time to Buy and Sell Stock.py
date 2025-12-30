# Leetcode Exercise 121: Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        firstprice = prices[0]
        for price in prices:
            if firstprice > price:
                firstprice = price
            else:
                profit.append(price - firstprice)
        if profit == []:
            profit.append(0)
        result = max(profit)
        return result
        