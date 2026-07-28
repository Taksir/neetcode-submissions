import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict() # num2frequency
        heap = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for i in range(k):
            freq, val = heapq.heappop(heap)
            ans.append(val)

        return ans
