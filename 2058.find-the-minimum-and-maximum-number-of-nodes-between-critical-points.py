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
        
        min_dist = float('inf')
        first_cp_idx = -1
        prev_cp_idx = -1
        
        curr_idx = 1
        prev_node = head
        curr_node = head.next
        
        while curr_node.next:
            next_node = curr_node.next
            
            # Check if curr_node is a critical point (local maxima or minima)
            is_critical = False
            if (curr_node.val > prev_node.val and curr_node.val > next_node.val) or \
               (curr_node.val < prev_node.val and curr_node.val < next_node.val):
                is_critical = True
            
            if is_critical:
                if first_cp_idx == -1:
                    first_cp_idx = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_cp_idx)
                prev_cp_idx = curr_idx
            
            prev_node = curr_node
            curr_node = next_node
            curr_idx += 1
            
        if min_dist == float('inf'):
            return [-1, -1]
        
        max_dist = prev_cp_idx - first_cp_idx
        return [min_dist, max_dist]
# @lc code=end