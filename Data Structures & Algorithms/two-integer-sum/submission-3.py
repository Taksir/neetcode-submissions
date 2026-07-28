class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        haveSeen = dict()

        for i, n in enumerate(nums):
            if (target - n) in haveSeen:
                return [haveSeen[target - n], i]
            haveSeen[n] = i
            