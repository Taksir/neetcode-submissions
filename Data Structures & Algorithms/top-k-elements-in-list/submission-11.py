class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        counts = collections.defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        for count, freq in counts.items():
            freqs[freq].append(count)

        small_k = 0
        results = []
        for i in range(len(freqs) - 1, -1, -1):
            for item in freqs[i]:
                results.append(item)
                small_k += 1
                if small_k == k:
                    return results

                    