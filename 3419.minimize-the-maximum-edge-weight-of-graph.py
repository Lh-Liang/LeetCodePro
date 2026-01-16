#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # Binary search on the answer
        # For a given max weight, check if it's possible to build a valid graph
        
        # Sort edges by weight
        edges.sort(key=lambda x: x[2])
        
        def is_valid(max_weight):
            # Build graph with edges having weight <= max_weight
            # For each node, keep only threshold number of edges with smallest weights
            
            # Group edges by source node
            from collections import defaultdict
            import heapq
            
            graph = defaultdict(list)
            
            for a, b, w in edges:
                if w <= max_weight:
                    # Use max heap to keep only threshold smallest weights
                    # Python has min heap, so we negate weights
                    heapq.heappush(graph[a], (-w, b))
                    if len(graph[a]) > threshold:
                        heapq.heappop(graph[a])
            
            # Build final adjacency list with only allowed edges
            adj = defaultdict(list)
            for node in graph:
                for _, dest in graph[node]:
                    adj[node].append(dest)
            
            # Check if node 0 is reachable from all other nodes using BFS/DFS
            # This is equivalent to checking if all nodes can reach node 0 in reverse graph
            
            # Build reverse graph
            reverse_graph = defaultdict(list)
            for node in adj:
                for neighbor in adj[node]:
                    reverse_graph[neighbor].append(node)
            
            # BFS from node 0 in reverse graph to see which nodes can reach 0
            visited = [False] * n
            queue = [0]
            visited[0] = True
            reachable_count = 1
            
            while queue:
                node = queue.pop(0)
                for neighbor in reverse_graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        reachable_count += 1
                        queue.append(neighbor)
            
            return reachable_count == n
        
        # Binary search on possible weights
        left, right = 0, edges[-1][2] if edges else 0
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
# @lc code=end