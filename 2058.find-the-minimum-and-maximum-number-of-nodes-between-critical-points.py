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
        prev_node = head
        curr_node = head.next
        
        while curr_node.next:
            prev_val = prev_node.val
            curr_val = curr_node.val
            next_val = curr_node.next.val
            
            # Check for critical point
            if (curr_val > prev_val and curr_val > next_val) or \n               (curr_val < prev_val and curr_val < next_val):
                
                if first_idx == -1:
                    first_idx = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_idx)
                
                prev_idx = curr_idx
            
            prev_node = curr_node
            curr_node = curr_node.next
            curr_idx += 1
            
        # If fewer than two critical points found
        if first_idx == -1 or prev_idx == first_idx:
            return [-1, -1]
            
        return [int(min_dist), prev_idx - first_idx]
# @lc code=end