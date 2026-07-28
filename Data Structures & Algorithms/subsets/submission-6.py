# lesson. this is a binary inclusion-exlusion idea
# if we had a j in range(i, len(nums)) like that, the exclusion would be built-into the for loop structure
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def dfs(i):
            ans.append(subset.copy())

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()

        dfs(0)
        return ans