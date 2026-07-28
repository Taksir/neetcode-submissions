class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(i, target):
            if target == 0:
                res.append(subset.copy())
                return
            if i >= len(candidates) or target < 0:
                return

            subset.append(candidates[i])
            dfs(i + 1, target - candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            subset.pop()
            dfs(i + 1, target)

        dfs(0, target)
        return res