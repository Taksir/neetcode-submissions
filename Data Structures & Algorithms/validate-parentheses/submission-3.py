class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {']':'[', '}':'{', ')':'('}
        stack = []
        for ch in s:
            if ch in mapper:
                if not stack or stack[-1] != mapper[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack
