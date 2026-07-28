import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        heap = []
        for n, freq in counter.items():
            heapq.heappush(heap, [-freq, n])

        ans = []
        for i in range(k):
            freq, n = heapq.heappop(heap)
            ans.append(n)
        
        return ans
