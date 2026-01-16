#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        
        # Build adjacency list for children of each node
        children = [[] for _ in range(n)]
        for i in range(1, n):  # Skip root node (index 0)
            children[parent[i]].append(i)
        
        # Precompute subtree information
        # For each node, we'll store the DFS string of its subtree
        subtree_strings = [''] * n
        
        # First DFS to compute subtree strings
        def dfs_subtree(node):
            # Start with empty string for this subtree
            subtree_str = ''
            
            # Process all children in order
            for child in children[node]:
                subtree_str += dfs_subtree(child)
            
            # Append current node's character
            subtree_str += s[node]
            
            subtree_strings[node] = subtree_str
            return subtree_str
        
        # Compute all subtree strings
        dfs_subtree(0)
        
        # For each node, we need to check if its subtree string is palindrome
        result = [False] * n
        
        for i in range(n):
            substr = subtree_strings[i]
            result[i] = substr == substr[::-1]
        
        return result
# @lc code=end