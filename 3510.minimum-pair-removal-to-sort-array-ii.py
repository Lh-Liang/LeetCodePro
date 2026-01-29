#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
import heapq

class Node:
    __slots__ = ['val', 'id', 'prev', 'next', 'removed']
    def __init__(self, val, node_id):
        self.val = val
        self.id = node_id
        self.prev = None
        self.next = None
        self.removed = False

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        nodes = [Node(nums[i], i) for i in range(n)]
        for i in range(n):
            if i > 0: nodes[i].prev = nodes[i-1]
            if i < n - 1: nodes[i].next = nodes[i+1]
        
        violations = 0
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                violations += 1
        
        if violations == 0:
            return 0
            
        pq = []
        # Tuple format: (sum, left_node_id, left_node_object)
        # Using left_node_id for leftmost tie-break and left_node_object for access
        # Note: In Python 3, if sum and id are identical, it tries to compare the objects.
        # We can wrap the object or use a unique counter to prevent object comparison.
        for i in range(n - 1):
            heapq.heappush(pq, (nodes[i].val + nodes[i+1].val, nodes[i].id, nodes[i]))

        ops = 0
        while pq:
            s, node_id, u = heapq.heappop(pq)
            
            # Validation
            if u.removed or not u.next or u.next.removed:
                continue
            v = u.next
            if s != u.val + v.val:
                continue
            
            ops += 1
            
            # Atomic Violation Removal
            if u.prev and u.prev.val > u.val: violations -= 1
            if u.val > v.val: violations -= 1
            if v.next and v.val > v.next.val: violations -= 1
            
            # Merge
            u.val = s
            v.removed = True
            u.next = v.next
            if v.next:
                v.next.prev = u
                
            # Atomic Violation Re-addition
            if u.prev and u.prev.val > u.val: violations += 1
            if u.next and u.val > u.next.val: violations += 1
            
            if violations == 0:
                return ops
                
            # Push new potential pairs
            if u.prev:
                heapq.heappush(pq, (u.prev.val + u.val, u.prev.id, u.prev))
            if u.next:
                heapq.heappush(pq, (u.val + u.next.val, u.id, u))
                
        return ops
# @lc code=end