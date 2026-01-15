#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        from collections import defaultdict
        
        n = len(nums)
        
        # Union-Find with path compression
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # Build connectivity from swaps
        for p, q in swaps:
            union(p, q)
        
        # Group indices by their connected component
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
        
        # Calculate maximum alternating sum
        result = 0
        for indices in components.values():
            values = [nums[i] for i in indices]
            even_count = sum(1 for i in indices if i % 2 == 0)
            
            # Sort values in descending order
            values.sort(reverse=True)
            
            # Add top even_count values (for even indices)
            for i in range(even_count):
                result += values[i]
            # Subtract remaining values (for odd indices)
            for i in range(even_count, len(values)):
                result -= values[i]
        
        return result
# @lc code=end