from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        deq = deque()
        l = r = 0

        for r in range(len(nums)):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)

            if deq[0] < l:
                deq.popleft()
            
            if r >= k - 1:
                ans.append(nums[deq[0]])
                l += 1
                
        return ans