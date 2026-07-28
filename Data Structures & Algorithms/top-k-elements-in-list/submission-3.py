import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1 # storing frequency

        heap = []
        for key, value in counts.items():
            heapq.heappush(heap, [-value, key])

        ans = []
        for i in range(k):
            value, key = heapq.heappop(heap)
            ans.append(key)

        return ans