#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        # Step 1: Create an adjacency list for the tree
        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        
        # Step 2: Precompute all paths using BFS for efficient querying
        def bfs(root):
            parent = {root: None}
            depth = {root: 0}
            queue = deque([root])
            while queue:
                node = queue.popleft()
                for neighbor, weight in adj_list[node]:
                    if neighbor not in parent:
                        parent[neighbor] = (node, weight)
                        depth[neighbor] = depth[node] + 1
                        queue.append(neighbor)
            return parent, depth
        
        # Precompute parent and depth information from root node (0)
        parent_info, depth_info = bfs(0)
        
        # Function to find LCA of two nodes using parent information and depths
        def find_lca(u, v):
            if depth_info[u] < depth_info[v]:
                u, v = v, u
            
            while depth_info[u] > depth_info[v]:
                u = parent_info[u][0]
            
            while u != v:
                u = parent_info[u][0]
                v = parent_info[v][0]
            
            return u
        
        # Function to find weighted median given a path from u to v via LCA lca
        def find_weighted_median(u, v):
            lca = find_lca(u, v)
            path_weight = 0
            weights_u_to_lca = []  # Weights from u to LCA inclusive
            weights_v_to_lca = []  # Weights from v to LCA exclusive (reverse order)									# Ascend from u to lca storing weights along path.	while u != lca:	parent_node_u , weight_u_via_parent= parent_info[u]	weights_u_to_lca.append(weight_u_via_parent) 	u=parent_node_u continue until reach common ancestor node (lca).	Ascend similarly from query end vertex(v) towards lca storing edge-weight(s) encountered until reach this shared ancestor point between both vertices(v,u).	while(v!=lca):	parent_node_v , weight_v_via_parent=parent_info[v]	weights_v_to_lca.append(weight_v_via_parent) # Note : Reverse order due descending upwards towards ancestor before reversing again when calculating cumulative weight sums later on . This enables easier summation calculation(s).	v=parent_node_v continue until meet common intermediary node shared with previous traversal upwards prior within function call stack .# Total path weight is sum of both traversals' cumulative weights :path_weight=sum(weights_u_to_lca)+sum(weights_v_to_lca)# Calculate half-path-weight threshold value we seek surpassing/meeting during traversal summation(s):half_weight_threshold=path_weight/2.0current_sum_weight=0.0for idx,node_weight in enumerate(weights_u_to_lca):current_sum_weight+=node_weightif current_sum_weight>=half_weight_threshold:return idx+1if not idx+1==len(weights_u_to_lca)-1 else [u,lca][idx==len(weights_u_to_lca)-1]for node_wgt_idx,node_wgt_rvs in enumerate(reversed(weights_v_to_lca)):current_sum_weight+=node_wgt_rvsif current_sum_weight>=half_weight_threshold:return [lca,v][node_wgt_idx==len(reversed(weights_v_to_lca))-1]return-1# should not hit under constraints .    results=[]for query_start_vertex ,query_end_vertex in queries :results.append(find_weighted_median(query_start_vertex ,query_end_vertex))      return results