class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        tmp_stack = self.prices[:]
        count = 0
        while tmp_stack and price >= tmp_stack[-1]:
            tmp_stack.pop()
            count += 1
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)