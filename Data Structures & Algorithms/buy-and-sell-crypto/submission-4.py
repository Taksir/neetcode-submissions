class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = float('inf')

        for p in prices:
            if p < minP:
                minP = p
            else:
                maxP = max(maxP, p - minP)
        
        return maxP