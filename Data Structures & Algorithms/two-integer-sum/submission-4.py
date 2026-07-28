class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenSoFar = dict()
        for i, n in enumerate(nums):
            comp = target - n
            if comp in seenSoFar:
                return [seenSoFar[comp], i]
            seenSoFar[n] = i
