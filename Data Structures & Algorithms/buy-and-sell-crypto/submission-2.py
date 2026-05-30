class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price =prices[0]
        max_pro = 0
        for i in range(len(prices)):
            min_price= min(min_price, prices[i])
            temp = prices[i] - min_price
            max_pro = max(max_pro,temp)
        return max_pro
                   