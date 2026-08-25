
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')
        profit = 0
        for p in prices:
            buy_price = min(buy_price, p)
            profit = max(p - buy_price, profit)
        return profit
