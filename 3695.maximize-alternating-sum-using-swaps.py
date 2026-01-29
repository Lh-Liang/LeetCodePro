#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        parent = list(range(n))
        rank = [0] * n
        
        def find(i):
            root = i
            while parent[root] != root:
                root = parent[root]
            while parent[i] != root:
                next_node = parent[i]
                parent[i] = root
                i = next_node
            return root
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_i] = root_j
                    rank[root_j] += 1
        
        for u, v in swaps:
            union(u, v)
            
        from collections import defaultdict
        components_values = defaultdict(list)
        components_even_counts = defaultdict(int)
        
        for i in range(n):
            root = find(i)
            components_values[root].append(nums[i])
            if i % 2 == 0:
                components_even_counts[root] += 1
        
        total_sum = 0
        for root in components_values:
            vals = components_values[root]
            vals.sort(reverse=True)
            num_even = components_even_counts[root]
            
            # Largest values to even positions
            for i in range(num_even):
                total_sum += vals[i]
            # Smallest values to odd positions
            for i in range(num_even, len(vals)):
                total_sum -= vals[i]
                
        return total_sum
# @lc code=end