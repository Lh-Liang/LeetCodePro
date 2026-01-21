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
        last_idx = -1
        min_dist = float('inf')
        
        prev_val = head.val
        curr = head.next
        curr_idx = 1
        
        while curr.next:
            next_val = curr.next.val
            # Check if current node is a local maxima or minima
            if (prev_val < curr.val > next_val) or (prev_val > curr.val < next_val):
                if first_idx == -1:
                    first_idx = curr_idx
                else:
                    # Update minimum distance between adjacent critical points
                    min_dist = min(min_dist, curr_idx - last_idx)
                last_idx = curr_idx
            
            prev_val = curr.val
            curr = curr.next
            curr_idx += 1
            
        # If fewer than two critical points were found
        if first_idx == -1 or first_idx == last_idx:
            return [-1, -1]
        
        # max_dist is always first vs last; min_dist is the smallest adjacent gap found
        return [int(min_dist), last_idx - first_idx]
# @lc code=end