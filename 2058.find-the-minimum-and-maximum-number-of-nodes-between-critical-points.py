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
        # Initialize variables
        first_cp_index = last_cp_index = -1
        min_distance = float('inf')
        current_index = 0
        critical_points = []
        
        # Pointer setup for iteration
        prev_node = None
        current_node = head
        
        # Traverse the linked list to find all critical points
        while current_node and current_node.next:
            next_node = current_node.next
            if prev_node:
                # Check if current node is a local maxima or minima
                if (current_node.val > prev_node.val and current_node.val > next_node.val) or \
                   (current_node.val < prev_node.val and current_node.val < next_node.val):
                    if first_cp_index == -1:
                        first_cp_index = current_index  # First critical point found
                    else:
                        # Calculate distance from last critical point found
                        min_distance = min(min_distance, current_index - last_cp_index)
                    last_cp_index = current_index  # Update last critical point index
                    
                    # Store index of this critical point for maximum distance calculation later
                    critical_points.append(current_index)
            
            # Move to the next sequence in the list
            prev_node = current_node
            current_node = next_node
            current_index += 1
        
        # If fewer than two critical points were found, return [-1, -1]
        if len(critical_points) < 2:
            return [-1, -1]
        
        # Calculate max distance as difference between first and last critical point indices
        max_distance = critical_points[-1] - critical_points[0]
        
        return [min_distance, max_distance]
# @lc code=end