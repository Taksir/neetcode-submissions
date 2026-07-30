# do simulation on paper
# maxheap of size 26 tracks frequency
# if cur_time has valid task, pop from q and add back to maxHeap
# if task is popped from maxHeap, its passed to q with cooldown + time only
# only if its new freq is not 0. Keeps going until both empty
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
            # if not maxHeap and q:  # Skip idle time to next available task
            #     time = q[0][1]
            # next line will be elif instead of if
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq < -1:
                    q.append((freq + 1, time + n + 1))
            time += 1
        
        return time

