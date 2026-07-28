import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        heap = []
        for key, value in count.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans