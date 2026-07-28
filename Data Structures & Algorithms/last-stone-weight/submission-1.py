import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            w1, w2 = -heapq.heappop(stones), -heapq.heappop(stones)
            if w1 > w2:
                heapq.heappush(stones, w2 - w1)
            
        return -stones[0] if stones else 0