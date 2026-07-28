class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, ss):
            if i == len(nums):
                ans.append(ss.copy())
                return 
            
            dfs(i + 1, ss + [nums[i]])
            dfs(i + 1, ss)
        
        dfs(0, [])
        return ans