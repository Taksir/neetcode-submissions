import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(x*x + y*y, (x,y)) for x, y in points] # (dist, point)
        heapq.heapify(points)
        ans = []
        for i in range(k):
            _, (x, y) = heapq.heappop(points)
            ans.append([x, y])
        return ans