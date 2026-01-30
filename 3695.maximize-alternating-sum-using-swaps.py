#
# @lc app=leetcode id=3695 lang=python3
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
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
        
        n = len(nums)
        parent = list(range(n))
        rank = [0] * n
        
        for pi, qi in swaps:
            union(pi, qi)
        
        components = {}
        for i in range(n):
            root = find(i)
            if root not in components:
                components[root] = []
            components[root].append(nums[i])
        
n   for component in components.values():
n   component.sort()  # sort each component

    max_sum = 0
    index = 0
    used_components_indexes = {i: 0 for i in components.keys()}
nfor _ in range(n):
n    min_component_key = min(
n          used_components_indexes.keys(), 
n          key=lambda k: (components[k][used_components_indexes[k]], k) if used_components_indexes[k] < len(components[k]) else (float('inf'), k)
n    )
n   value_to_use_from_component=min_component_key

    curr_value=components[min_component_key][used_components_indexes[min_component_key]]
nused_components_indexes[min_component_key]+=1

    if index % 2 == 0:
total_sum += curr_value
else:
total_sum -= curr_value
index += 1 
n 
n return max_sum 
total_sum #@lc code=end