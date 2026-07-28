# heapify sorts in-place. do not use return!
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-1 *(points[i][0] * points[i][0] + points[i][1] * points[i][1]), points[i][0], points[i][1]) for i in range(len(points))]
        heapq.heapify(heap)
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []

        while heap:
            dist, x, y = heapq.heappop(heap)
            res.append(([x,y]))
        
        return res
        