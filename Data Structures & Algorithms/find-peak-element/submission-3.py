
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            left = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            right = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')

            if left < nums[mid] and nums[mid] > right:
                return mid
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1 # nums[mid] > nums[right]

        return -1