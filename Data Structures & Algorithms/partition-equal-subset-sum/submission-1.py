# if total = odd, return false
# sort in decreasing order
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse = True)
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2

        memo = [[-1] * (target + 1) for _ in range(len(nums) + 1)]
        def dfs(i, total):
            if total == target:
                return True
            if i == len(nums) or total > target:
                return False
            if memo[i][total] != -1:
                return bool(memo[i][total])
            # did not take element at i; did take element at i
            if dfs(i + 1, total) or dfs(i + 1, total + nums[i]):
                memo[i][total] = 1
                return True
            memo[i][total] = 0
            return False
        
        return dfs(0, 0)