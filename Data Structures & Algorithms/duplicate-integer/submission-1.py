class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return not len(list(set(nums))) == len(nums)
        mySet = set()
        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)

        return False