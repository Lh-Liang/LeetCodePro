#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
from typing import List
from collections import defaultdict, deque

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        # Step 1: Initialize a Union-Find data structure to manage connected components from swaps
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
        
        # Step 2: Apply all swaps to union-find structure to form connected components
        for p, q in swaps:
            union(p, q)
        
        # Step 3: Group nums by their connected component roots found by union-find structure
        components = defaultdict(list)
        for i in range(len(nums)):
            root = find(i)
            components[root].append(nums[i])
        
        # Step 4 & 5: Sort each component group to maximize alternating sum when used optimally across entire array.
        sorted_nums = [0] * len(nums) # To reconstruct optimal num array from sorted components globally.
       for key in components:    components[key].sort(reverse=True) # Sort descending for optimal selection at even indices first.index = 0for key in components:    size = len(components[key])    for i in range(size):        sorted_nums[index + i * 2] = components[key][i]    for i in range(size):        if index + i * 2 + 1 < len(sorted_nums):            sorted_nums[index + i * 2 + 1] = -components[key][i]    index += size * 2# Step 6: Calculate the alternating sum using reconstructed nums array.max_sum = sum(sorted_nums[i] if i % 2 == 0 else -sorted_nums[i] for i in range(len(sorted_nums)))return max_sum# @lc code=end