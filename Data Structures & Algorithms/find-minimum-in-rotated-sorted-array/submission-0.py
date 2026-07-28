class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if mid > nums[r] -> smallest is in right part
        # otherwise: smallest is in left part
        l, r = 0, len(nums) - 1
        res = float('infinity')
        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])

            mid = l + (r-l) // 2
            res = min(res, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return res