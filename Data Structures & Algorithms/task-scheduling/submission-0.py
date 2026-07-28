import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-x for x in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            if q and q[0][1] == time:
                freq, t2 = q.popleft()
                heapq.heappush(maxHeap, freq)
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq < -1:
                    q.append((freq + 1, time + n + 1))
            time += 1
        
        return time

