import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for i, p in enumerate(points):
            dist = p[0] ** 2 + p[1] ** 2
            heapq.heappush(heap, [-dist, p[0], p[1]])
            if len(heap) > k:
                heapq.heappop(heap)
            
        ans = []
        while heap:
            dist, p, q = heapq.heappop(heap)
            ans.append([p,q])
        return ans