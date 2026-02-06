#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#
from typing import List
from collections import defaultdict, deque
import heapq

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        def check_reachability_and_constraints(max_weight):
            # Build adjacency list with valid edges (<= max_weight)
            adj_list = defaultdict(list)
            in_degree = [0] * n
            for u, v, w in edges:
                if w <= max_weight:
                    adj_list[u].append((w, v))
                    in_degree[v] += 1
            
            # Check reverse reachability using BFS from node 0 to all other nodes
            queue = deque([0])
            visited = set(queue)
            while queue:
                current = queue.popleft()
                for _, neighbor in adj_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        
            # Verify all nodes are reachable by checking visited set size
            if len(visited) != n:
                return False
            
            # Verify outgoing edge constraint using priority queues for each node's adjacency list
            for u in range(n):
                if len(adj_list[u]) > threshold:
                    min_heap = [(w, v) for w, v in adj_list[u]]
                    heapq.heapify(min_heap)
                    adj_list[u] = [heapq.heappop(min_heap) for _ in range(threshold)]
                
            return True  # If all conditions are satisfied with current max_weight
        
        # Binary search over possible max weights (1 to max(edge weights))
        left, right = 1, max(w for _, _, w in edges)
        answer = -1  # Default answer if no feasible solution found
        while left <= right:
            mid = (left + right) // 2
            if check_reachability_and_constraints(mid):
                answer = mid  # Update answer with feasible mid value
                right = mid - 1  # Try smaller weights by reducing upper bound of search space
            else:
                left = mid + 1  # Increase allowable weight as current mid is not feasible due to constraints violation or unreachable nodes to node zero.
        return answer