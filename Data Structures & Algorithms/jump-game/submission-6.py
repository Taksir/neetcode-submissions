class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = deque([0])
        visited = set([0]) # dont forget to put 0!
        while q:
            idx = q.popleft()
            if idx == len(nums) - 1:
                return True
            for i in range(min(len(nums), idx + 1 + nums[idx]) - 1, idx, -1):
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        
        return False
            