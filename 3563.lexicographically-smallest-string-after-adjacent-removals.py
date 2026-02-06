#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and (ord(stack[-1]) == ord(char) - 1 or ord(stack[-1]) == ord(char) + 1 or (stack[-1] == 'z' and char == 'a') or (stack[-1] == 'a' and char == 'z')):
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
# @lc code=end