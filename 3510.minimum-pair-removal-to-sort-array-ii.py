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
        if n < 2:
            return 0
        
        # Doubly linked list to track adjacent elements
        L = [i - 1 for i in range(n)]
        R = [i + 1 for i in range(n)]
        val = list(nums)
        version = [0] * n
        
        pq = []
        violations = 0
        
        # Initialize violations and priority queue
        for i in range(n - 1):
            if val[i] > val[i+1]:
                violations += 1
            heapq.heappush(pq, (val[i] + val[i+1], i, version[i], version[i+1]))
            
        ops = 0
        while violations > 0 and pq:
            s, i, v_i, v_j = heapq.heappop(pq)
            
            # Check if this pair is still valid
            j = R[i]
            if j == n or version[i] != v_i or version[j] != v_j:
                continue
            
            # Perform merge operation
            ops += 1
            h = L[i]
            k = R[j]
            
            # Remove violations involving the nodes being merged
            if h != -1 and val[h] > val[i]:
                violations -= 1
            if val[i] > val[j]:
                violations -= 1
            if k != n and val[j] > val[k]:
                violations -= 1
            
            # Update value and versions
            val[i] = val[i] + val[j]
            version[i] += 1
            version[j] += 1 # Effectively invalidates pairs involving j
            
            # Update linked list pointers
            R[i] = k
            if k != n:
                L[k] = i
            
            # Add new violations
            if h != -1 and val[h] > val[i]:
                violations += 1
            if k != n and val[i] > val[k]:
                violations += 1
            
            # Push new potential pairs to the heap
            if h != -1:
                heapq.heappush(pq, (val[h] + val[i], h, version[h], version[i]))
            if k != n:
                heapq.heappush(pq, (val[i] + val[k], i, version[i], version[k]))
                
        return ops
# @lc code=end