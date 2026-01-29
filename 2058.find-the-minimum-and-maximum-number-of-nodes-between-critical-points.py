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
        
        first_cp_idx = -1
        prev_cp_idx = -1
        min_dist = float('inf')
        
        # Start from the second node (index 1)
        prev_val = head.val
        curr = head.next
        idx = 1
        
        while curr.next:
            next_val = curr.next.val
            
            # Identify if current node is a critical point
            is_maxima = curr.val > prev_val and curr.val > next_val
            is_minima = curr.val < prev_val and curr.val < next_val
            
            if is_maxima or is_minima:
                if first_cp_idx == -1:
                    first_cp_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_cp_idx)
                
                prev_cp_idx = idx
            
            prev_val = curr.val
            curr = curr.next
            idx += 1
            
        # If we found fewer than 2 critical points
        if min_dist == float('inf'):
            return [-1, -1]
        
        max_dist = prev_cp_idx - first_cp_idx
        return [int(min_dist), int(max_dist)]
# @lc code=end