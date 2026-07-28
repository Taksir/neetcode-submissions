# # apparently there is a O(m) space solution. this is O(n) space.
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest = 0
#         charset = set()
#         l = r = 0
#         while r < len(s):
#             if s[r] in charset: # moving l logic
#                 while s[l] != s[r]: # no need to update 'longest' when we r truncating
#                     charset.remove(s[l])
#                     l += 1
#                 l += 1
#             else:
#                 longest = max(longest, r - l + 1) # ONLY UPDATE WHEN we extend

#             charset.add(s[r])
#             r += 1 # r always moving

#         return longest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        charset = set()
        l = r = 0
        while r < len(s):
            while s[r] in charset: # moving l logic
                charset.remove(s[l])
                l += 1

            charset.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1 # r always moving

        return longest