class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        idx = 0

        while idx != slow:
            idx = nums[idx]
            slow = nums[slow]

        return slow