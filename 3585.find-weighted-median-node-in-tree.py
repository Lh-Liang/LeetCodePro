#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list for the tree
        from collections import defaultdict
        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))

        # Step 2: Preprocess with DFS to calculate cumulative weights
        cumulative_weights = [0] * n
        parents = [-1] * n

        def dfs(node, parent):
            for neighbor, weight in adj_list[node]:
                if neighbor == parent:
                    continue
                parents[neighbor] = node
                cumulative_weights[neighbor] = cumulative_weights[node] + weight
                dfs(neighbor, node)

        dfs(0, -1)

        # Helper function to find LCA of two nodes u and v
        def find_lca(u, v):
            ancestors_u = set()
            while u != -1:
                ancestors_u.add(u)
                u = parents[u]
            while v not in ancestors_u:
                v = parents[v]
            return v

        results = []
        for uj, vj in queries:
            # Step 3 & 4: Calculate total path weight and find LCA of uj and vj
            lca = find_lca(uj, vj)
            total_path_weight = (cumulative_weights[uj] + cumulative_weights[vj] - 2 * cumulative_weights[lca])
            half_weight = total_path_weight / 2.0
            # Step 5: Traverse from uj towards vj and find weighted median node
            current_node = uj if cumulative_weights[uj] > cumulative_weights[vj] else vj
            while current_node != lca:
                next_node = parents[current_node]
                edge_weight = abs(cumulative_weights[current_node] - cumulative_weights[next_node])
                if edge_weight >= half_weight:
                    results.append(current_node)
                    break
                half_weight -= edge_weight
                current_node = next_node
            else:
                results.append(current_node) # In case median is at or after LCA
        return results
# @lc code=end