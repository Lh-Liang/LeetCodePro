# @lc code=start
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # Step 1: Sort edges by weight
        sorted_edges = sorted(edges, key=lambda x: x[2])
        
        # Utility function for checking connectivity from node 0
        def canConnect(max_weight):
            # Create adjacency list with only allowed edges and enforce threshold constraint
            adj_list = [[] for _ in range(n)]
            out_degree = [0] * n  # Track outgoing degree of each node
            for u, v, w in sorted_edges:
                if w <= max_weight and out_degree[u] < threshold:
                    adj_list[u].append(v)
                    out_degree[u] += 1
            
            # Perform BFS/DFS from node 0
            visited = [False] * n
            stack = [0]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for neighbor in adj_list[node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
            
            # Check if all nodes are reachable from node 0 and threshold respected
            return all(visited) and all(deg <= threshold for deg in out_degree)
        
        # Binary search over possible maximum weights
        left, right = 0, len(sorted_edges) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            max_weight = sorted_edges[mid][2]
            if canConnect(max_weight):
                result = max_weight
                right = mid - 1
            else:
                left = mid + 1
        return result # Return final result or -1 if no valid configuration found
# @lc code=end