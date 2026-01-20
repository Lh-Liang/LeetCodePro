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
        
        prev = head
        curr = head.next
        index = 1  # 0-based index, head is 0, curr starts at 1
        
        first_critical_idx = -1
        last_critical_idx = -1
        min_dist = float('inf')
        
        while curr.next:
            # Check for local maxima or minima
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                
                if first_critical_idx == -1:
                    first_critical_idx = index
                else:
                    min_dist = min(min_dist, index - last_critical_idx)
                
                last_critical_idx = index
            
            prev = curr
            curr = curr.next
            index += 1
            
        if min_dist == float('inf'):
            return [-1, -1]
            
        return [min_dist, last_critical_idx - first_critical_idx]
# @lc code=end