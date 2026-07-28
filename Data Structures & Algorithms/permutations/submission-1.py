class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(nums): 
            if not nums:
                return [[]]
            permutes = helper(nums[1 : ]) # maybe pass ranges instead of slicing
            higher_perms = []
            for p in permutes:
                for i in range(len(p) + 1):
                    temp = p.copy()
                    temp.insert(i, nums[0])
                    higher_perms.append(temp)
            return higher_perms.copy()

        return helper(nums)