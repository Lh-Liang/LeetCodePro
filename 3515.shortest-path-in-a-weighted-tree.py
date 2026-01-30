#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        import heapq
        
        # Step 1: Construct adjacency list and weights dictionary
        graph = defaultdict(list)
        weight = {}
        for u, v, w in edges:
            graph[u].append(v)
            graph[v].append(u)
            weight[(u, v)] = w
            weight[(v, u)] = w
        
        # Step 2: Function to update edge weights
        def update_edge(u: int, v: int, w_prime: int):
            weight[(u, v)] = w_prime
            weight[(v, u)] = w_prime
        
        # Step 3: Function to compute shortest path using Dijkstra's algorithm
        def compute_shortest_path(x: int) -> int:
            min_heap = [(0, 1)]  # (current_distance, current_node)
            distances = {i: float('inf') for i in range(1, n + 1)}
            distances[1] = 0
            visited = set()
            while min_heap:
                dist, node = heapq.heappop(min_heap)
                if node in visited:
                    continue
                visited.add(node)
                if node == x:
                    return dist
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        new_dist = dist + weight[(node, neighbor)]
                        if new_dist < distances[neighbor]:
                            distances[neighbor] = new_dist
                            heapq.heappush(min_heap, (new_dist, neighbor))
            return -1  # If node x is unreachable (should not happen in valid tree)
        
        result = []
        for query in queries:
            if query[0] == 1:
                _, u, v, w_prime = query
                update_edge(u, v, w_prime)  # Update edge weight as specified by query[1,u,v,w']
            elif query[0] == 2:
                _, x = query  # Compute shortest path from root (1) to x as specified by query[2,x]
                result.append(compute_shortest_path(x))
                                                                                                    \t\t\t\t\t\t\t\t\t\t\tttttttttttttttttttttttttttttttttttttttttrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrreeeeeeeeturn result     \nnnnnnnnnnnnnnnnnnnnnnnnnn