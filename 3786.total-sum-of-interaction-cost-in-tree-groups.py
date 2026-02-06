#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        from collections import defaultdict, deque
        
        # Step 1: Build the adjacency list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Step 2 & 4: Function to calculate interaction cost within a single group using BFS
        def bfs_cost(nodes):
            if len(nodes) < 2:
                return 0
            total_cost = 0
            for start in nodes:
                queue = deque([(start, 0)])
                visited = {start}
                while queue:
                    current, dist = queue.popleft()
                    for neighbor in adj_list[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, dist + 1))
                            if neighbor in nodes:
                                total_cost += dist + 1
            return total_cost // 2 # Each path is counted twice (u-v and v-u)
        
        # Step 3: Group nodes by their group label
        group_to_nodes = defaultdict(list)
        for node in range(n):
            group_to_nodes[group[node]].append(node)
        
        total_interaction_cost = 0
        
        # Step 5: Calculate interaction costs within each group and aggregate them
        for nodes in group_to_nodes.values():
            total_interaction_cost += bfs_cost(nodes)

        return total_interaction_cost
# @lc code=end