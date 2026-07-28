class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = deque([0])
        visited = set([0])
        while q:
            idx = q.popleft()
            if idx == len(nums) - 1:
                return True
            for i in range(idx + 1, min(len(nums), idx + 1 + nums[idx])):
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        
        return False
            