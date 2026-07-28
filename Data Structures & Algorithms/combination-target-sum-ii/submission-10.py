class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                ans.append(subset.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subset.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return ans