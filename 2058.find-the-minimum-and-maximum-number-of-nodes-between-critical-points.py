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
        # A critical point requires at least 3 nodes to exist.
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        # Start from the second node (index 1)
        prev_node = head
        curr_node = head.next
        curr_idx = 1
        
        while curr_node.next:
            p_val = prev_node.val
            c_val = curr_node.val
            n_val = curr_node.next.val
            
            is_critical = False
            # Local Maxima
            if c_val > p_val and c_val > n_val:
                is_critical = True
            # Local Minima
            elif c_val < p_val and c_val < n_val:
                is_critical = True
            
            if is_critical:
                if first_cp == -1:
                    first_cp = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_cp)
                prev_cp = curr_idx
            
            # Move to the next node
            prev_node = curr_node
            curr_node = curr_node.next
            curr_idx += 1
            
        # If fewer than two critical points were found
        if first_cp == -1 or prev_cp == first_cp:
            return [-1, -1]
            
        return [int(min_dist), prev_cp - first_cp]
# @lc code=end