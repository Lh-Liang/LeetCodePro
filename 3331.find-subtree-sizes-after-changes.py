#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        original_adj = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p != -1:
                original_adj[p].append(i)
        
        new_parent = list(parent)
        
        # ancestors[char_code] = node_index
        # Initialize with -1 indicating no ancestor for that char yet
        ancestors = [-1] * 26
        
        def dfs_find_parents(u):
            char_code = ord(s[u]) - ord('a')
            closest_ancestor = ancestors[char_code]
            
            if closest_ancestor != -1:
                new_parent[u] = closest_ancestor
            
            # Save current state to backtrack
            ancestors[char_code] = u
            
            for v in original_adj[u]:
                dfs_find_parents(v)
            
            # Backtrack
            ancestors[char_code] = closest_ancestor

        # Start DFS from root (node 0)
        dfs_find_parents(0)
        
        # Build new tree adjacency list
        new_adj = [[] for _ in range(n)]
        for i, p in enumerate(new_parent):
            if p != -1:
                new_adj[p].append(i)
        
        subtree_sizes = [0] * n
        
        # DFS to calculate subtree sizes
        # Using iterative DFS to avoid recursion limit issues for deep trees, 
        # though standard recursion is usually fine for 10^5 in Python depending on settings.
        # Let's use standard recursion with setrecursionlimit just in case.
        import sys
        sys.setrecursionlimit(200000)
        
        def dfs_calc_size(u):
            size = 1
            for v in new_adj[u]:
                size += dfs_calc_size(v)
            subtree_sizes[u] = size
            return size

        dfs_calc_size(0)
        
        return subtree_sizes
# @lc code=end