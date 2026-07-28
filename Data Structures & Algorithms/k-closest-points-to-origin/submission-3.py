import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[p[0]**2 + p[1]**2, p[0], p[1]] for p in points]
        heapq.heapify(heap)

        ans = []
        while k > 0:
            d, p, q = heapq.heappop(heap)
            k -= 1
            ans.append([p,q])

        return ans
        
