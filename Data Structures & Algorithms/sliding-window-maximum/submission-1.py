import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        res = [-heap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         heap = []
#         output = []
#         for i in range(len(nums)):
#             heapq.heappush(heap, (-nums[i], i))
#             if i >= k - 1:
#                 while heap[0][1] <= i - k:
#                     heapq.heappop(heap)
#                 output.append(-heap[0][0])
#         return output