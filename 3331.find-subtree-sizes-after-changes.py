#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
from typing import List
import collections

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = [-1] * n
        # tracks the current path's ancestors for each character 'a'-'z'
        char_ancestors = [[] for _ in range(26)]
        
        # Iterative DFS to find new parents based on original tree ancestors
        # (node, child_iterator)
        stack = [(0, iter(adj[0]))]
        
        # Process root
        char_idx = ord(s[0]) - ord('a')
        char_ancestors[char_idx].append(0)
        
        while stack:
            u, children = stack[-1]
            try:
                v = next(children)
                v_char_idx = ord(s[v]) - ord('a')
                
                # Find closest ancestor with same character
                if char_ancestors[v_char_idx]:
                    new_parent[v] = char_ancestors[v_char_idx][-1]
                else:
                    new_parent[v] = parent[v]
                
                # Push to stack and update char path
                char_ancestors[v_char_idx].append(v)
                stack.append((v, iter(adj[v])))
                
            except StopIteration:
                # Finished exploring all children of u
                u_char_idx = ord(s[u]) - ord('a')
                char_ancestors[u_char_idx].pop()
                stack.pop()
        
        # Build the new tree structure
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        # Calculate subtree sizes in the new tree using iterative post-order
        ans = [1] * n
        # Standard iterative post-order: reverse of a modified pre-order
        order = []
        process_stack = [0]
        while process_stack:
            u = process_stack.pop()
            order.append(u)
            for v in new_adj[u]:
                process_stack.append(v)
        
        # Process in reverse pre-order (which is post-order)
        for u in reversed(order):
            if u != 0:
                p = new_parent[u]
                ans[p] += ans[u]
                
        return ans
# @lc code=end