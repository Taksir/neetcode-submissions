class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        numlist= []

        def dfs(target, j, numlist):
            if target == 0:
                ans.append(numlist.copy())
                return
            
            if target < 0:
                return
            
            for i in range(j, len(nums)):
                dfs(target - nums[i], i, numlist + [nums[i]])
            
        dfs(target, 0, numlist)
        return ans
