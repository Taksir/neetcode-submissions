class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        for i in range(2, N):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[N-1], cost[N-2])

# # O(n) and O(n) -> my solution
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         arr = [0] * (len(cost) + 1)

#         for i in range(2, len(arr)):
#             arr[i] = min(arr[i - 2] + cost[i - 2], arr[i - 1] + cost[i - 1])

#         return arr[-1]