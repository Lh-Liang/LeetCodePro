#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        if n == 0:
            return []
            
        # Original adjacency list
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        # Find new parents based on original ancestors
        # We use DFS to track the nearest ancestor for each character
        new_parent = [-1] * n
        char_stacks = [[] for _ in range(26)]
        
        # Iterative DFS to find new parents
        # stack element: (node, is_processed)
        stack = [(0, False)]
        while stack:
            u, processed = stack.pop()
            char_idx = ord(s[u]) - ord('a')
            
            if not processed:
                # Determine new parent for node u
                if u == 0:
                    new_parent[u] = -1
                else:
                    if char_stacks[char_idx]:
                        new_parent[u] = char_stacks[char_idx][-1]
                    else:
                        new_parent[u] = parent[u]
                
                # Mark as processed and push back to pop after children
                char_stacks[char_idx].append(u)
                stack.append((u, True))
                
                # Push children to stack
                for v in adj[u]:
                    stack.append((v, False))
            else:
                # Post-order: remove node from character stack
                char_stacks[char_idx].pop()
                
        # Construct the new tree adjacency list
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        # Calculate subtree sizes iteratively using post-order traversal
        subtree_size = [1] * n
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in new_adj[u]:
                stack.append(v)
        
        # Process nodes in reverse pre-order (which is post-order)
        for u in reversed(order):
            if u != 0:
                p = new_parent[u]
                subtree_size[p] += subtree_size[u]
                
        return subtree_size
# @lc code=end