#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def find_path(start, end):
            # DFS to find path from start to end
            def dfs(node, parent):
                if node == end:
                    return [node]
                
                for neighbor, weight in graph[node]:
                    if neighbor != parent:
                        path = dfs(neighbor, node)
                        if path:
                            return [node] + path
                
                return None
            
            return dfs(start, -1) or []
        
        answer = []
        for u, v in queries:
            path_nodes = find_path(u, v)
            
            # Calculate cumulative weights for each node
            cumulative_weights = [0]
            for i in range(1, len(path_nodes)):
                prev_node = path_nodes[i - 1]
                curr_node = path_nodes[i]
                # Find edge weight between prev_node and curr_node
                for neighbor, weight in graph[prev_node]:
                    if neighbor == curr_node:
                        cumulative_weights.append(cumulative_weights[-1] + weight)
                        break
            
            # Find the first node where cumulative weight >= half of total
            total_weight = cumulative_weights[-1]
            half_weight = total_weight / 2
            
            for i, node in enumerate(path_nodes):
                if cumulative_weights[i] >= half_weight:
                    answer.append(node)
                    break
        
        return answer
# @lc code=end