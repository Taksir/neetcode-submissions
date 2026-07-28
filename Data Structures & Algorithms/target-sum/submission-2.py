class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 # add upto 0 in one way

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cursum, count in dp.items():
                next_dp[cursum + nums[i]] += count
                next_dp[cursum - nums[i]] += count
            dp = next_dp

        return dp[target]