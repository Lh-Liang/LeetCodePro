#
# @lc app=leetcode id=2058 lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # A critical point needs a previous and next node, so list must have at least 3 nodes
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_idx = -1
        prev_idx = -1
        min_dist = float('inf')
        
        # Tracking previous value to identify local maxima/minima
        prev_val = head.val
        curr = head.next
        idx = 1 # 0-indexed position of curr
        
        while curr.next:
            next_val = curr.next.val
            
            # Local Maxima or Local Minima
            is_critical = (curr.val > prev_val and curr.val > next_val) or \
                          (curr.val < prev_val and curr.val < next_val)
            
            if is_critical:
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx
            
            prev_val = curr.val
            curr = curr.next
            idx += 1
            
        # If fewer than 2 critical points were found
        if first_idx == -1 or prev_idx == first_idx:
            return [-1, -1]
            
        return [min_dist, prev_idx - first_idx]
# @lc code=end