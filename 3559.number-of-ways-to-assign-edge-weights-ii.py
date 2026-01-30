#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        MOD = 10**9 + 7
        n = len(edges) + 1
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def bfs(u, v):
            queue = deque([(u, 0)])
            visited = {u}
            while queue:
                node, depth = queue.popleft()
                if node == v:
                    return depth % 2 == 1 # Return True if path length is odd.
                for neighbor in tree[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, depth + 1))
            return False # No valid path found. Should not happen as it’s a tree.
        
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0) # Path from node to itself has zero length, hence no assignment makes it odd.
            else:
                answer.append(2 if bfs(u,v) else 0) # If path length is even (bfs returns False), no valid assignment exists. Otherwise (True), two assignments exist. 
        return [a % MOD for a in answer]
# @lc code=end