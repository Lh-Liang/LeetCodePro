#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Function to find root of an element with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Function to union two sets by rank
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        n = len(nums)
        parent = list(range(n))
        rank = [0] * n
        
        # Union-Find to group swappable indices
        for u, v in swaps:
            union(u, v)
        
        # Group numbers by their connected components using union-find roots
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
        
        # For each component, sort numbers and place them optimally for maximum alternating sum
        result_nums = nums[:]
        for indices in components.values():
            sorted_indices = sorted(indices)
            sorted_values = sorted(result_nums[i] for i in indices)
            # Place larger values on even index positions and smaller on odd index positions
            for i, idx in enumerate(sorted_indices):
                result_nums[idx] = sorted_values[i]
                
        # Calculate the alternating sum based on optimized arrangement
        max_alternating_sum = 0
        for i in range(n):
            if i % 2 == 0:
                max_alternating_sum += result_nums[i]
            else:
                max_alternating_sum -= result_nums[i]
                
        return max_alternating_sum
# @lc code=end