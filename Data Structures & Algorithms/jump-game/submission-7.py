#  my own bfs solution, uses O(n) space. but greedy is O(1)
# bottom solution is greedy with no extra space.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = deque([0])
        visited = set([0]) # dont forget to put 0!
        while q:
            idx = q.pop() 
            if idx == len(nums) - 1:
                return True
            for i in range(idx + 1, min(len(nums), idx + 1 + nums[idx])):
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        
        return False
            
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         goal = len(nums) - 1

#         for i in range(len(nums) -2, -1, -1):
#             if nums[i] + i >= goal:
#                 goal = i
#         return goal == 0