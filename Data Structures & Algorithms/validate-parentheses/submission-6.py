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
        return len(stack) == 0
'''
# OPTIMIZATION 1: The Odd-Length Guard Clause (Early Exit). 
# At the absolute top of your function, add: `if len(s) % 2 != 0: return False`. 
# If the string length is odd, it is mathematically impossible for every bracket 
# to have a matching pair, allowing you to skip the loop entirely for invalid inputs.

# OPTIMIZATION 2: Pythonic Stack Truthiness. 
# You can replace your final line `return len(s) == 0` with `return not stack`. 
# In Python, empty lists naturally evaluate to False at the C-level, making 
# `not stack` slightly faster than calculating the exact length of the list.

# OPTIMIZATION 3: The "Push the Expected Closer" Alternative. 
# Instead of pushing opening brackets and looking them up against the dict later, 
# you can use an if-elif block to push the *matching closing* bracket onto the stack 
# the moment you see an opener. Then, your closing check simplifies to a direct match: 
# `if not stack or stack.pop() != ch: return False`. This completely eliminates the dictionary.

# OPTIMIZATION 4: Hashing Overhead Awareness. 
# Your `ch in matches` lookup takes O(1) time, which is optimal. However, if an 
# interviewer asks you to optimize it even further without using dictionaries, 
# you can achieve the exact same O(1) speed using standard string lookups, like 
# checking index positions in matching string pairs (e.g., ` openers = "({[" `).
'''      
class Solution:
    def isValid(self, s: str) -> bool:
        # OPTIMIZATION 1: Early exit for odd lengths
        if len(s) % 2 != 0:
            return False
            
        stack = []

        for ch in s:
            # When you see an opener, push the expected closer onto the stack
            if ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            # If it's a closer, it MUST match the top of the stack exactly
            elif not stack or stack.pop() != ch:
                return False

        # OPTIMIZATION 2: Return using clean truthiness
        return not stack       
         