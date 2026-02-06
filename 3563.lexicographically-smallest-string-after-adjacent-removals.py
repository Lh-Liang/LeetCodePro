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
            while stack and ((ord(stack[-1]) - ord(char)) % 26 == 1 or (ord(char) - ord(stack[-1])) % 26 == 1):
                stack.pop()
            stack.append(char)
        return ''.join(stack)
# @lc code=end