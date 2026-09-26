class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < minimum_price:
                minimum_price = price
            else:
                profit = price - minimum_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit