#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        # Build adjacency list from edges
        adj_list = defaultdict(list)
        edge_weights = {}
        for u, v, w in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            edge_weights[(u, v)] = edge_weights[(v, u)] = w
        
        # Function to perform BFS/DFS for shortest path calculation
        def bfs_shortest_path(x):
            queue = deque([(1, 0)]) # (node, current_distance)
            visited = set()
            while queue:
                current_node, current_dist = queue.popleft()
                if current_node == x:
                    return current_dist
                visited.add(current_node)
                for neighbor in adj_list[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, current_dist + edge_weights[(current_node, neighbor)]))
            return float('inf')  # In case no path found which shouldn't happen because it's a tree.
        
        answer = []
        " Process each query " " as either update or compute shortest path " " "for query in queries:" " if query[0] == 1:" " _, u, v, w_prime = query # Update weight of edge (u,v) to w' " " edge_weights[(u,v)] = edge_weights[(v,u)] = w_prime " else:" _, x = query # Compute shortest path from root node (1) to x " answer.append(bfs_shortest_path(x)) " return answer # @lc code=end