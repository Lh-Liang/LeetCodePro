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
        
        first_cp_index = -1
        prev_cp_index = -1
        min_dist = float('inf')
        
        prev_node = head
        curr_node = head.next
        curr_index = 1
        
        while curr_node.next:
            next_node = curr_node.next
            is_critical = False
            
            # Check for local maxima
            if curr_node.val > prev_node.val and curr_node.val > next_node.val:
                is_critical = True
            # Check for local minima
            elif curr_node.val < prev_node.val and curr_node.val < next_node.val:
                is_critical = True
            
            if is_critical:
                if first_cp_index == -1:
                    first_cp_index = curr_index
                else:
                    min_dist = min(min_dist, curr_index - prev_cp_index)
                prev_cp_index = curr_index
            
            prev_node = curr_node
            curr_node = next_node
            curr_index += 1
            
        if min_dist == float('inf'):
            return [-1, -1]
            
        max_dist = prev_cp_index - first_cp_index
        return [min_dist, max_dist]
# @lc code=end