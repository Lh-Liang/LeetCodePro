#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        from collections import defaultdict
        
        def is_palindrome(st):
            return st == st[::-1]
        
        n = len(parent)
        tree = defaultdict(list)
        for child, par in enumerate(parent):
            if par != -1:
                tree[par].append(child)
        
        def dfs(node):
            dfsStr = []
            def helper(x):
                for child in sorted(tree[x]):  # Ensure children are processed in order
                    helper(child)
                dfsStr.append(s[x])
            helper(node)
            return ''.join(dfsStr)
        
        answer = [False] * n
        for i in range(n):
            current_dfsStr = dfs(i)
            answer[i] = is_palindrome(current_dfsStr)
        
        return answer
# @lc code=end