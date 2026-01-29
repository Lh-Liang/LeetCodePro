#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        from collections import defaultdict
        
        # Step 2: Build adjacency list
        tree = defaultdict(list)
        n = len(parent)
        for i in range(1, n):
            tree[parent[i]].append(i)
            
        def is_palindrome(string):
            return string == string[::-1]
        
        # The result array
        answer = [False] * n
        
        # Step 3: Implement recursive DFS to construct dfsStr and check palindromes
        def dfs(node):
            dfsStr = []
            def visit(x):
                for child in sorted(tree[x]):
                    visit(child)
                dfsStr.append(s[x])
            visit(node)
            return ''.join(dfsStr)
        
        # Step 5: Iterate over all nodes
        for i in range(n):
            dfsStr = dfs(i)
            answer[i] = is_palindrome(dfsStr)
            
        return answer
# @lc code=end