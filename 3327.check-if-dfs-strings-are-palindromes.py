#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#
# @lc code=start
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        from collections import defaultdict
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        # Ensure children are in increasing order
        for ch in children:
            ch.sort()
        def dfs(x, res):
            for y in children[x]:
                dfs(y, res)
            res.append(s[x])
        answer = [False] * n
        for i in range(n):
            res = []
            dfs(i, res)
            dfsStr = ''.join(res)
            answer[i] = (dfsStr == dfsStr[::-1])
        return answer
# @lc code=end