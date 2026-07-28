import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = collections.deque()
        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if r >= k - 1:
                l += 1
                ans.append(nums[q[0]])
                if q[0] < l:
                    q.popleft()
            
        return ans
