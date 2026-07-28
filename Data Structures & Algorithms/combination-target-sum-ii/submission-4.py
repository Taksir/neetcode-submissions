class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(i, target, subset):
            if target == 0:
                ans.append(subset.copy())
                return
            elif target < 0:
                return
            
            for j in range(i+1, len(candidates)):
# The correct way to skip duplicates at the same recursion level 
# is to skip an element only if it is the same as the previous
# element AND it isn’t the first one we’re trying at this level. 
                if j >= i+2 and candidates[j] == candidates[j-1]:
                    continue
                if target - candidates[j] < 0:
                    break
                subset.append(candidates[j])
                dfs(j, target-candidates[j], subset) # use append and pop instead
                subset.pop()
            
        dfs(-1, target, [])
        return ans
