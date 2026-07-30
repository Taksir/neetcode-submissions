import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        maxHeap = [-x for x in list(count.values())]
        heapq.heapify(maxHeap)
        deq = collections.deque()
        time = 0
        while maxHeap or deq:
            while deq and time >= deq[0][1]: # insert (freq, time)
                freq, t = deq.popleft()
                heapq.heappush(maxHeap, freq)

            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq < -1:
                    freq += 1
                    deq.append((freq, time + n + 1))
            time += 1

        return time
