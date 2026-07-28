import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-weight for weight in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            heaviest1, heaviest2 = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            if heaviest1 > heaviest2:
                heapq.heappush(stones, -1 * (heaviest1 - heaviest2))

        return -1 * stones[0] if stones else 0