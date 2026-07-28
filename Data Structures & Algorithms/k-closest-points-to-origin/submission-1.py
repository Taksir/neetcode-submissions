# heapify sorts in-place. do not use return!
# slightly worse because O(nlogn). full heap, then remove
# better is O(nlogk), dont allow it to grow beyond k size
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for p, q in points:
            dist = p**2 + q**2
            heapq.heappush(heap, [-dist, p, q])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        while heap:
            dist, x, y = heapq.heappop(heap)
            res.append(([x,y]))
        
        return res
        