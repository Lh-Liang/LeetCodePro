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
        tree = defaultdict(list)
        for i in range(1, n):
            tree[parent[i]].append(i)
        
        def is_palindrome(string):
            return string == string[::-1]
        
        def dfs(node):
            dfsStr.append(s[node])
            for child in sorted(tree[node]):
                dfs(child)

        answer = [False] * n
        for i in range(n):
            dfsStr = []  # Reset dfsStr for new DFS call
            dfs(i)  # Perform DFS starting from node i
            answer[i] = is_palindrome(''.join(dfsStr))
        return answer
# @lc code=end