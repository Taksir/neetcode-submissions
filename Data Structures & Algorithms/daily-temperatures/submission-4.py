class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        stack = []
        ans = [0] * len(t)
        for i, temp in enumerate(t):

            while stack and stack[-1][0] < temp:
                tt, idx = stack.pop()
                ans[idx] = i - idx

            stack.append((temp, i))

        return ans
