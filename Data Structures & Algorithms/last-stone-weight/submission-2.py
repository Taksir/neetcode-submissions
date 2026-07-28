import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            a, b = -heapq.heappop(stones), -heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, -(a - b))
        return 0 if not stones else -stones[0]