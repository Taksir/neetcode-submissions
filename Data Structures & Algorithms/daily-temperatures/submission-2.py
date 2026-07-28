class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp: # since we always popping, check nonempty stack
                index, dayTemp = stack.pop()
                answer[index] = i - index
            
            stack.append((i, temp))

        return answer
