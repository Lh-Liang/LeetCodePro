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
        first_cp = -1
        prev_cp = -1
        
        curr_idx = 1
        prev_node = head
        curr_node = head.next
        
        while curr_node.next:
            is_critical = False
            # Local Maxima
            if curr_node.val > prev_node.val and curr_node.val > curr_node.next.val:
                is_critical = True
            # Local Minima
            elif curr_node.val < prev_node.val and curr_node.val < curr_node.next.val:
                is_critical = True
            
            if is_critical:
                if first_cp == -1:
                    first_cp = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_cp)
                prev_cp = curr_idx
            
            prev_node = curr_node
            curr_node = curr_node.next
            curr_idx += 1
            
        if min_dist == float('inf'):
            return [-1, -1]
        
        return [min_dist, prev_cp - first_cp]
# @lc code=end