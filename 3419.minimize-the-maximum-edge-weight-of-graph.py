#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
from typing import List, DefaultDict
from collections import defaultdict, deque

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # Step 1: Prepare sorted unique weights for binary search
        weights = sorted(set(w for _,_,w in edges))
        edge_buckets = defaultdict(list)
        for a, b, w in edges:
            edge_buckets[a].append((w, b))
        
        def is_feasible(max_weight):
            # Step 2a: For each node, select outgoing edges <= max_weight, up to 'threshold' smallest
            out_edges = defaultdict(list)
            for a in range(n):
                valid = [(w, b) for (w, b) in edge_buckets[a] if w <= max_weight]
                valid.sort()
                for (w, b) in valid[:threshold]:
                    out_edges[a].append(b)
                # Step 2b: Enforce threshold constraint
                if len(out_edges[a]) > threshold:
                    return False
            # Step 3: Reverse graph for reachability check (all nodes should reach 0)
            rev_edges = defaultdict(list)
            for u in out_edges:
                for v in out_edges[u]:
                    rev_edges[v].append(u)
            # Step 4: BFS from node 0 in reversed graph
            seen = set([0])
            dq = deque([0])
            while dq:
                node = dq.popleft()
                for nei in rev_edges[node]:
                    if nei not in seen:
                        seen.add(nei)
                        dq.append(nei)
            # Step 5: Verify all nodes can reach node 0
            return len(seen) == n
        
        # Step 6: Binary search over unique weights
        left, right, answer = 0, len(weights) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if is_feasible(weights[mid]):
                answer = weights[mid]
                right = mid - 1
            else:
                left = mid + 1
        # Step 7: Double-check that answer is valid (already ensured by is_feasible)
        return answer
# @lc code=end