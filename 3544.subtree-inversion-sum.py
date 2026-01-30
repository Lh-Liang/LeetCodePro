#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
class Solution:
    def subtreeInversionSum(self, edges, nums, k):
        from collections import defaultdict, deque
        
        # Step 1: Construct adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: DFS to calculate initial subtree sums and parent information
        n = len(nums)
        subtree_sum = [0] * n
        visited = [False] * n
        parent = [-1] * n
        depth = [0] * n
        
        def dfs(node, d):
            visited[node] = True
            total_sum = nums[node]
            depth[node] = d
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    parent[neighbor] = node
                    total_sum += dfs(neighbor, d + 1)
            subtree_sum[node] = total_sum
            return total_sum
        
        dfs(0, 0)  # Start DFS from root node 0 with initial depth 0
        
        # Step 3 & 4: Identify nodes for inversion and respect distance constraint `k`
        def can_invert(node, selected_nodes):
            # Check if any selected node is within distance k of current node.
            queue = deque([(node, 0)])
            visited_check = set([node])
            while queue:
                current, dist = queue.popleft()
                if dist >= k:
                    continue
                for neighbor in tree[current]:
                    if neighbor in visited_check or neighbor == parent[current]:
                        continue
                    if neighbor in selected_nodes:
                        return False
                    visited_check.add(neighbor)
                    queue.append((neighbor, dist + 1))
            return True
       
       # Step 5: Strategically select nodes for inversion based on potential gain and constraints.
       result_max_sum = sum(nums)  # Initial sum without any inversions
       selected_nodes = set()
       for i in range(n):
           if can_invert(i, selected_nodes) and subtree_sum[i] < 0:
               result_max_sum += -2 * subtree_sum[i]
               selected_nodes.add(i)
       
       return result_max_sum   
# @lc code=end