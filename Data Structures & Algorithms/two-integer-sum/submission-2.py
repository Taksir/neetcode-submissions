class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        haveSeenSoFar = dict()

        for i in range(len(nums)):
            if (target - nums[i]) in haveSeenSoFar:
                return [haveSeenSoFar[target - nums[i]], i]
            haveSeenSoFar[nums[i]] = i
