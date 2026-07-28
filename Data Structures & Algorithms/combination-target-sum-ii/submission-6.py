class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        candidates.sort()
        def dfs(i, subset, target):
            if target == 0: 
                ans.append(subset.copy())
                return
            
            for j in range(i+1, len(candidates)):
                if j >= i + 2 and candidates[j] == candidates[j-1]:
                    continue
                if target - candidates[j] >= 0:
                    subset.append(candidates[j])
                    dfs(j, subset, target - candidates[j])
                    subset.pop()

        dfs(-1, [], target)
        return ans