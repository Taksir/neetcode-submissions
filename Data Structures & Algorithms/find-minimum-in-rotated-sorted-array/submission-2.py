# mid > right, so smallest on right subpart
# else, smallest on left subpart
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]