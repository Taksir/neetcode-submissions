class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenSoFar = {}

        for i, num in enumerate(nums):
            if target - num in seenSoFar:
                return [seenSoFar[target - num], i]

            seenSoFar[num] = i

            