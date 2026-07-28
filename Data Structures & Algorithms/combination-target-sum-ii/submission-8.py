class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        candidates.sort()
        def dfs(i, subset, target):
            if target == 0: 
                ans.append(subset.copy())
                return
            
            for j in range(i, len(candidates)):
                if j >= i + 1 and candidates[j] == candidates[j-1]:
                    continue
                
                if target - candidates[j] < 0:
                    break
                subset.append(candidates[j])
                dfs(j+1, subset, target - candidates[j])
                subset.pop()

        dfs(0, [], target)
        return ans