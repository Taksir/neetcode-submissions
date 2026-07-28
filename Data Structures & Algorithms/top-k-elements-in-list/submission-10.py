class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        
        for n, count in freq_map.items():
            freqs[count].append(n)
        
        ans = []
        r = len(freqs) - 1
        while k > 0:
            if freqs[r]:
                ans.append(freqs[r].pop())
                k -= 1
                if k == 0:
                    break
            if not freqs[r]:
                r -= 1

        return ans