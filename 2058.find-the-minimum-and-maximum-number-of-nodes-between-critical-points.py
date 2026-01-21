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
        # A critical point requires at least 3 nodes (prev, curr, next).
        # The constraints guarantee at least 2 nodes.
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_cp_idx = -1
        prev_cp_idx = -1
        min_dist = -1
        
        prev_node = head
        curr_node = head.next
        curr_idx = 1
        
        # Iterate through the list starting from the second node
        # until the second-to-last node.
        while curr_node.next:
            next_node = curr_node.next
            
            # Check if the current node is a local maxima or local minima
            is_maxima = curr_node.val > prev_node.val and curr_node.val > next_node.val
            is_minima = curr_node.val < prev_node.val and curr_node.val < next_node.val
            
            if is_maxima or is_minima:
                if first_cp_idx == -1:
                    # Record the very first critical point found
                    first_cp_idx = curr_idx
                else:
                    # Calculate distance from the previous critical point
                    dist = curr_idx - prev_cp_idx
                    if min_dist == -1 or dist < min_dist:
                        min_dist = dist
                
                # Update the index of the last critical point found
                prev_cp_idx = curr_idx
            
            # Move pointers to the next position
            prev_node = curr_node
            curr_node = next_node
            curr_idx += 1
            
        # If fewer than 2 critical points were found, min_dist remains -1
        if min_dist == -1:
            return [-1, -1]
        
        # Maximum distance is always between the first and last critical point
        max_dist = prev_cp_idx - first_cp_idx
        
        return [min_dist, max_dist]
# @lc code=end