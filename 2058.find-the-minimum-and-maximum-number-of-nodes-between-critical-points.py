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
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        prev_val = head.val
        curr = head.next
        idx = 1
        
        while curr.next:
            next_val = curr.next.val
            # Check if current node is a critical point
            is_maxima = curr.val > prev_val and curr.val > next_val
            is_minima = curr.val < prev_val and curr.val < next_val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = idx
                else:
                    min_dist = min(min_dist, idx - prev_cp)
                prev_cp = idx
            
            prev_val = curr.val
            curr = curr.next
            idx += 1
            
        if first_cp == prev_cp: # Fewer than two critical points
            return [-1, -1]
            
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]

# @lc code=end