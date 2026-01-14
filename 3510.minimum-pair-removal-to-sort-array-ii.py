#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        values = list(nums)
        deleted = [False] * n
        prev_node = [i - 1 for i in range(n)]
        next_node = [i + 1 for i in range(n)]
        
        bad_count = sum(1 for i in range(n - 1) if values[i] > values[i + 1])
        
        if bad_count == 0:
            return 0
        
        pairs = SortedList()
        for i in range(n - 1):
            pairs.add((values[i] + values[i + 1], i))
        
        operations = 0
        
        while bad_count > 0:
            min_sum, left = pairs.pop(0)
            
            if deleted[left]:
                continue
            
            right = next_node[left]
            if right >= n or deleted[right]:
                continue
            
            if values[left] + values[right] != min_sum:
                continue
            
            prev_n = prev_node[left]
            next_n = next_node[right]
            
            # Remove old bad pairs
            if prev_n >= 0 and values[prev_n] > values[left]:
                bad_count -= 1
            if values[left] > values[right]:
                bad_count -= 1
            if next_n < n and values[right] > values[next_n]:
                bad_count -= 1
            
            # Merge
            deleted[right] = True
            values[left] = min_sum
            next_node[left] = next_n
            if next_n < n:
                prev_node[next_n] = left
            
            # Add new bad pairs
            if prev_n >= 0 and values[prev_n] > values[left]:
                bad_count += 1
            if next_n < n and values[left] > values[next_n]:
                bad_count += 1
            
            # Add new pairs
            if prev_n >= 0:
                pairs.add((values[prev_n] + values[left], prev_n))
            if next_n < n:
                pairs.add((values[left] + values[next_n], left))
            
            operations += 1
        
        return operations
# @lc code=end