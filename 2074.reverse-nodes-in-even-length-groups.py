#
# @lc app=leetcode id=2074 lang=python3
#
# [2074] Reverse Nodes in Even Length Groups
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # The first group always has length 1 (odd), so it's never reversed.
        # We start 'prev' at the last node of the first group.
        prev = head
        group_size = 2
        
        while prev.next:
            # Count the actual number of nodes in the current group
            count = 0
            temp = prev.next
            while temp and count < group_size:
                temp = temp.next
                count += 1
            
            if count % 2 == 0:
                # Reverse the group of 'count' nodes
                curr = prev.next
                # rev_prev starts as 'temp' (the node after the group) 
                # so that the new tail automatically points to the rest of the list
                rev_prev = temp
                rev_curr = curr
                for _ in range(count):
                    rev_next = rev_curr.next
                    rev_curr.next = rev_prev
                    rev_prev = rev_curr
                    rev_curr = rev_next
                
                # Connect the previous group's tail to the new head of this group
                prev.next = rev_prev
                # Update 'prev' to the current group's tail (which was the original head)
                prev = curr
            else:
                # Group length is odd, skip it by moving 'prev' to the end of the group
                for _ in range(count):
                    prev = prev.next
            
            # Move to the next group size
            group_size += 1
            
        return head
# @lc code=end