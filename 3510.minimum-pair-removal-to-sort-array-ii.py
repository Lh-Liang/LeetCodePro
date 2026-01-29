#
# @lc app=leetcode id=3510 lang=python3
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        class Node:
            def __init__(self, val: int, idx: int):
                self.val = val
                self.id = idx
                self.prev = None
                self.next = None
        nodes = [Node(nums[i], i) for i in range(n)]
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]
        # Initial violations
        violations = 0
        cur = nodes[0]
        while cur.next:
            if cur.val > cur.next.val:
                violations += 1
            cur = cur.next
        if violations == 0:
            return 0
        pq = []
        for i in range(n - 1):
            left = nodes[i]
            s = left.val + left.next.val
            heapq.heappush(pq, (s, left.id))
        ops = 0
        length = n
        while violations > 0 and length > 1:
            while pq:
                s, left_id = heapq.heappop(pq)
                left = nodes[left_id]
                right = left.next
                if right is not None and right.prev == left and left.val + right.val == s:
                    break
            else:
                break  # No valid pair
            # Compute delta violations (before merge)
            delta = 0
            p = left.prev
            if p:
                old_bad = 1 if p.val > left.val else 0
                new_bad = 1 if p.val > left.val + right.val else 0
                delta += new_bad - old_bad
            lr_bad = 1 if left.val > right.val else 0
            delta -= lr_bad
            right_next = right.next
            if right_next:
                rn_bad = 1 if right.val > right_next.val else 0
                delta -= rn_bad
                ln_bad = 1 if left.val + right.val > right_next.val else 0
                delta += ln_bad
            violations += delta
            # Perform merge
            left.val += right.val
            left.next = right_next
            if right_next:
                right_next.prev = left
            length -= 1
            ops += 1
            # Push new pairs
            if p:
                new_s = p.val + left.val
                heapq.heappush(pq, (new_s, p.id))
            if left.next:
                new_s = left.val + left.next.val
                heapq.heappush(pq, (new_s, left.id))
        return ops

# @lc code=end