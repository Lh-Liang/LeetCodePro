#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        values = nums[:]
        prev_node = [i - 1 for i in range(n)]
        next_node = [i + 1 for i in range(n)]
        next_node[-1] = -1
        
        heap = []
        pair_sum_map = {}
        
        bad_pairs = 0
        for i in range(n - 1):
            s = values[i] + values[i + 1]
            heapq.heappush(heap, (s, i))
            pair_sum_map[i] = s
            if values[i] > values[i + 1]:
                bad_pairs += 1
        
        operations = 0
        while bad_pairs > 0 and heap:
            s, i = heapq.heappop(heap)
            if i not in pair_sum_map or pair_sum_map[i] != s:
                continue
            
            j = next_node[i]
            old_val_i = values[i]
            old_val_j = values[j]
            
            p = prev_node[i]
            if p != -1 and p in pair_sum_map:
                if values[p] > old_val_i:
                    bad_pairs -= 1
                del pair_sum_map[p]
            
            if old_val_i > old_val_j:
                bad_pairs -= 1
            del pair_sum_map[i]
            
            k = next_node[j]
            if k != -1 and j in pair_sum_map:
                if old_val_j > values[k]:
                    bad_pairs -= 1
                del pair_sum_map[j]
            
            values[i] = old_val_i + old_val_j
            next_node[i] = k
            if k != -1:
                prev_node[k] = i
            
            if p != -1:
                new_sum = values[p] + values[i]
                heapq.heappush(heap, (new_sum, p))
                pair_sum_map[p] = new_sum
                if values[p] > values[i]:
                    bad_pairs += 1
            
            if k != -1:
                new_sum = values[i] + values[k]
                heapq.heappush(heap, (new_sum, i))
                pair_sum_map[i] = new_sum
                if values[i] > values[k]:
                    bad_pairs += 1
            
            operations += 1
        
        return operations
# @lc code=end