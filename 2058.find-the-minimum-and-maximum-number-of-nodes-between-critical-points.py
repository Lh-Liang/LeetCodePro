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
        
        first_idx = -1
        prev_idx = -1
        min_dist = float('inf')
        
        curr_idx = 1
        prev_val = head.val
        curr = head.next
        
        while curr.next:
            next_val = curr.next.val
            # Check if current node is a critical point
            is_max = curr.val > prev_val and curr.val > next_val
            is_min = curr.val < prev_val and curr.val < next_val
            
            if is_max or is_min:
                if first_idx == -1:
                    first_idx = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_idx)
                prev_idx = curr_idx
            
            # Move to the next node
            prev_val = curr.val
            curr = curr.next
            curr_idx += 1
            
        # If we found fewer than 2 critical points
        if first_idx == prev_idx:
            return [-1, -1]
            
        return [int(min_dist), prev_idx - first_idx]

# @lc code=end