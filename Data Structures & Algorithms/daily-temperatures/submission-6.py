class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]: # check if i need >=
                popped = stack.pop()
                ans[popped] = i - popped
            stack.append(i)

        return ans