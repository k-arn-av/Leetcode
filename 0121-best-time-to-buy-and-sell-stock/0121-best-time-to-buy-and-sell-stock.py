class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        left=0 #left is buy, right is sell
        for right in range(1,len(prices)):
            if prices[left]<prices[right]:
                currentProfit=prices[right]-prices[left]
                maxProfit=max(currentProfit, maxProfit)
            else:
                left=right

        return maxProfit
                