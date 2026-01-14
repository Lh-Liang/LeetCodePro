#
# @lc app=leetcode id=3785 lang=python3
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        
        # Build bipartite graph: position i can use value from source j if nums[j] != forbidden[i]
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if nums[j] != forbidden[i]:
                    graph[i].append(j)
        
        # Initialize matching arrays
        match_pos = [-1] * n  # match_pos[i] = j means position i gets value from source j
        match_val = [-1] * n  # match_val[j] = i means source j is assigned to position i
        
        # Augmenting path algorithm for bipartite matching
        def augment(u, visited):
            for v in graph[u]:
                if visited[v]:
                    continue
                visited[v] = True
                if match_val[v] == -1 or augment(match_val[v], visited):
                    match_pos[u] = v
                    match_val[v] = u
                    return True
            return False
        
        # First pass: match positions to themselves if possible (minimize swaps)
        for i in range(n):
            if nums[i] != forbidden[i]:
                match_pos[i] = i
                match_val[i] = i
        
        # Second pass: match remaining positions using augmenting paths
        for i in range(n):
            if match_pos[i] == -1:
                visited = [False] * n
                if not augment(i, visited):
                    return -1  # No perfect matching exists
        
        # Count cycles in the permutation
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = match_pos[j]
                cycles += 1
        
        # Minimum swaps = n - number of cycles
        return n - cycles
# @lc code=end