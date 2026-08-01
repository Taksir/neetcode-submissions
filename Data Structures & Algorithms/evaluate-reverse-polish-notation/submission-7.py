class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in "+-*/":
                a, b = stack.pop(), stack.pop()
                if ch == '+':
                    stack.append(a + b)
                elif ch == '*':
                    stack.append(a * b)
                elif ch == '-':
                    stack.append(b - a)
                elif ch == '/':
                    stack.append(int(float(b) / a))
            else:
                stack.append(int(ch))

        return stack[0]