#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        # Initialize union-find structures
        parent = list(range(len(nums)))
        rank = [0] * len(nums)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

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
        
        # Connect nodes according to swaps
        for pi, qi in swaps:
            union(pi, qi)
        
        # Group elements by their connected component roots
        from collections import defaultdict as ddict
        components = ddict(list)
        for i in range(len(nums)):
            components[find(i)].append(i)
        
        # Calculate maximum alternating sum by optimizing each component separately
        max_alternating_sum = 0
        for comp in components.values():
            # Sort values within this component to maximize alternating sum contribution
            numbers = sorted((nums[i] for i in comp), reverse=True)
            comp_sum = 0 
            # Calculate alternating sum for this sorted order 
            for idx, num in enumerate(numbers): 
                if idx % 2 == 0: 
                    comp_sum += num 
                else: 
                    comp_sum -= num 
            max_alternating_sum += comp_sum 
       
       # Return total maximum alternating sum across all components 
       return max_alternating_sum \\ @lc code=end