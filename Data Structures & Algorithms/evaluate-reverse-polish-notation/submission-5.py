class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == "+":
                stack.append(stack.pop() + stack.pop())
            elif tok == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif tok == '*':
                stack.append(stack.pop() * stack.pop())
            elif tok == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(tok))
        
        return stack[-1]
            