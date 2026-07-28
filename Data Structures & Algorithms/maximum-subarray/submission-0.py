class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum = 0
        for n in nums:
            curSum = max(curSum + n, n)
            maxSum = max(curSum, maxSum)
        return maxSum