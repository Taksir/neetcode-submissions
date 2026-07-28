class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = collections.deque()
        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]: #before appending r, remove smaller items
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                ans.append(nums[q[0]])
                l += 1

        return ans
