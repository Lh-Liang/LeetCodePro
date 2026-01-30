#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        def build_tree(edges, n):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree
        
        def compute_parity(tree, n):
            parity = [0] * n  # 0 for even, 1 for odd
            visited = [False] * n
            queue = deque([(0, 0)])  # (node, current_parity)
            visited[0] = True
            while queue:
                node, par = queue.popleft()
                parity[node] = par
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, 1 - par))
            return parity
        
        n = len(edges1) + 1  # number of nodes in the first tree
        m = len(edges2) + 1  # number of nodes in the second tree
        
        # Build trees from edge lists
        tree1 = build_tree(edges1, n)
        tree2 = build_tree(edges2, m)
        
        # Compute parity of paths from root (node 0) to all other nodes in both trees
        parity1 = compute_parity(tree1, n)
        parity2 = compute_parity(tree2, m)
        
        # Count nodes with even/odd parity in second tree
        count_even_2 = sum(1 for p in parity2 if p == 0)
        count_odd_2 = m - count_even_2
        
        result = []
        # For each node i in first tree calculate max target nodes after connection to any node in second tree
        for i in range(n):
            if parity1[i] == 0:
                result.append(count_even_2)  # Connecting an even-parity node with any even-parity node maintains even path length
            else:
                result.append(count_odd_2)   # Connecting an odd-parity node with any odd-parity node maintains even path length
                
        return result
# @lc code=end