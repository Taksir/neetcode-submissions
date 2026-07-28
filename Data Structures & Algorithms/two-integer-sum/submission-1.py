class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenSoFar = {}

        for i, n in enumerate(nums):
            if target - n in seenSoFar:
                return [seenSoFar[target - n], i]
            seenSoFar[n] = i
            