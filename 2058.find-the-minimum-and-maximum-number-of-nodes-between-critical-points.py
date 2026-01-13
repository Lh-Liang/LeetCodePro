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
        prev = head
        curr = head.next
        position = 1
        
        first_critical = -1
        last_critical = -1
        prev_critical = -1
        min_distance = float('inf')
        
        while curr and curr.next:
            next_node = curr.next
            
            # Check if current node is a critical point (local maxima or minima)
            is_critical = (curr.val > prev.val and curr.val > next_node.val) or \
                          (curr.val < prev.val and curr.val < next_node.val)
            
            if is_critical:
                if first_critical == -1:
                    # First critical point found
                    first_critical = position
                else:
                    # Update minimum distance between consecutive critical points
                    min_distance = min(min_distance, position - prev_critical)
                
                prev_critical = position
                last_critical = position
            
            prev = curr
            curr = curr.next
            position += 1
        
        # If fewer than 2 critical points
        if first_critical == -1 or first_critical == last_critical:
            return [-1, -1]
        
        max_distance = last_critical - first_critical
        
        return [min_distance, max_distance]
# @lc code=end