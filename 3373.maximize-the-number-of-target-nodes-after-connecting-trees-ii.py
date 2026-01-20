#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        adj1 = [[] for _ in range(n)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
            
        adj2 = [[] for _ in range(m)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
            
        # Helper to get bipartition counts and node colors
        def get_colors_and_counts(adj, num_nodes):
            colors = [-1] * num_nodes
            counts = [0, 0]
            colors[0] = 0
            counts[0] = 1
            stack = [0]
            
            while stack:
                u = stack.pop()
                current_color = colors[u]
                next_color = 1 - current_color
                
                for v in adj[u]:
                    if colors[v] == -1:
                        colors[v] = next_color
                        counts[next_color] += 1
                        stack.append(v)
            return colors, counts

        colors1, counts1 = get_colors_and_counts(adj1, n)
        _, counts2 = get_colors_and_counts(adj2, m)
        
        max_targets_from_tree2 = max(counts2[0], counts2[1])
        
        ans = []
        for i in range(n):
            # Targets in Tree 1 are nodes with the same color as i
            targets_in_tree1 = counts1[colors1[i]]
            # We always connect to a node in Tree 2 such that we get the max possible targets from Tree 2
            # Since we can pick any node v in Tree 2, we can always achieve max(counts2[0], counts2[1])
            # by picking v with appropriate parity.
            ans.append(targets_in_tree1 + max_targets_from_tree2)
            
        return ans
# @lc code=end