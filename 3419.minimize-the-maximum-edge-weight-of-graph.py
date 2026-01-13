#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        from collections import defaultdict, deque
        
        # Get all unique weights and sort them
        weights = sorted(set(w for _, _, w in edges))
        
        def canReachAll(maxWeight):
            # Filter edges by maxWeight
            filtered = [(a, b, w) for a, b, w in edges if w <= maxWeight]
            
            # Group by source node
            outgoing = defaultdict(list)
            for a, b, w in filtered:
                outgoing[a].append((b, w))
            
            # For each node, keep at most threshold edges (prioritize smaller weights)
            graph = defaultdict(list)
            for node in outgoing:
                outgoing[node].sort(key=lambda x: x[1])
                for i in range(min(threshold, len(outgoing[node]))):
                    graph[node].append(outgoing[node][i][0])
            
            # Reverse the graph to check reachability
            reversed_graph = defaultdict(list)
            for a in graph:
                for b in graph[a]:
                    reversed_graph[b].append(a)
            
            # BFS from node 0 in reversed graph
            visited = set([0])
            queue = deque([0])
            while queue:
                node = queue.popleft()
                for neighbor in reversed_graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            # Check if all nodes can reach node 0
            return len(visited) == n
        
        # Try each weight in ascending order
        for w in weights:
            if canReachAll(w):
                return w
        
        return -1
# @lc code=end