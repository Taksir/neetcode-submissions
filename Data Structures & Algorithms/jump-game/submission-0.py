class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = deque([0])

        while q:
            idx = q.popleft()
            if idx > len(nums) - 1:
                break
            if idx == len(nums) - 1:
                return True
            for i in range(idx + 1, idx + 1 + nums[idx]): # indices with 0 values are inserted
                q.append(i)

        return False
            