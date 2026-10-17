class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        stack = []
        for cur_price in prices:
            if stack:
                if cur_price < stack[-1]:
                    while stack and cur_price < stack[-1]:
                        stack.pop()
                    stack.append(cur_price)
                    continue
                else:
                    res += cur_price - stack[-1]
                    stack.pop()
                    stack.append(cur_price)
            else:
                stack.append(cur_price)
        return res