#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # Doubly linked list nodes: [val, prev_idx, next_idx]
        nodes = [[nums[i], i - 1, i + 1] for i in range(n)]
        nodes[n-1][2] = -1
        
        def is_sorted():
            curr = head
            while curr != -1 and nodes[curr][2] != -1:
                if nodes[curr][0] > nodes[nodes[curr][2]][0]:
                    return False
                curr = nodes[curr][2]
            return True

        # Track how many pairs are currently decreasing
        decreasing_count = 0
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                decreasing_count += 1
        
        if decreasing_count == 0:
            return 0

        # Heap stores (sum, left_id, version_left, version_right)
        # Using versions to handle invalidation
        versions = [0] * n
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (nodes[i][0] + nodes[i+1][0], i, i + 1, 0, 0))

        ops = 0
        head = 0
        
        while decreasing_count > 0:
            s, l, r, v_l, v_r = heapq.heappop(pq)
            
            # Check if this pair is still valid and adjacent
            if versions[l] != v_l or versions[r] != v_r or nodes[l][2] != r:
                continue
            
            # Perform operation
            ops += 1
            new_val = nodes[l][0] + nodes[r][0]
            
            # Update decreasing_count before merging
            # Check l's left neighbor
            prev = nodes[l][1]
            if prev != -1:
                if nodes[prev][0] > nodes[l][0]: decreasing_count -= 1
            # Check l and r
            if nodes[l][0] > nodes[r][0]: decreasing_count -= 1
            # Check r's right neighbor
            nxt = nodes[r][2]
            if nxt != -1:
                if nodes[r][0] > nodes[nxt][0]: decreasing_count -= 1
                
            # Merge r into l
            nodes[l][0] = new_val
            nodes[l][2] = nxt
            versions[l] += 1
            if nxt != -1:
                nodes[nxt][1] = l
                versions[nxt] += 1
            
            # Update decreasing_count after merging
            if prev != -1:
                if nodes[prev][0] > nodes[l][0]: decreasing_count += 1
            if nxt != -1:
                if nodes[l][0] > nodes[nxt][0]: decreasing_count += 1
            
            if decreasing_count == 0: break
            
            # Push new potential pairs
            if prev != -1:
                heapq.heappush(pq, (nodes[prev][0] + nodes[l][0], prev, l, versions[prev], versions[l]))
            if nxt != -1:
                heapq.heappush(pq, (nodes[l][0] + nodes[nxt][0], l, nxt, versions[l], versions[nxt]))
                
        return ops
# @lc code=end