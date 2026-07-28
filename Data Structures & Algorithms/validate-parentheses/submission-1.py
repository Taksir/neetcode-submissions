class Solution:
    def isValid(self, s: str) -> bool:
        matches = {']' : '[', '}' : '{', ')' : '('}
        stack = []

        for ch in s:
            if ch in matches:
                if stack and stack[-1] == matches[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0
            
                
         