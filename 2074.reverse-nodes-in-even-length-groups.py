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
        if not head:
            return head
        
        # The first group has length 1 (odd), so it's never reversed.
        # We start by tracking the end of the first group.
        prev_group_end = head
        expected_len = 2
        
        while prev_group_end.next:
            # Count the actual number of nodes in the current group
            count = 0
            curr = prev_group_end.next
            while curr and count < expected_len:
                curr = curr.next
                count += 1
            
            if count % 2 == 0:
                # Reverse the current group of 'count' nodes
                group_start = prev_group_end.next
                # rev_prev is initialized to 'curr', which is the first node of the next group
                rev_prev = curr 
                rev_curr = group_start
                for _ in range(count):
                    nxt = rev_curr.next
                    rev_curr.next = rev_prev
                    rev_prev = rev_curr
                    rev_curr = nxt
                
                # Connect the end of the previous group to the new head of this group
                prev_group_end.next = rev_prev
                # The old group_start is now the last node of this group
                prev_group_end = group_start
            else:
                # Group length is odd, skip reversal and move prev_group_end forward
                for _ in range(count):
                    prev_group_end = prev_group_end.next
            
            # Increment expected length for the next group
            expected_len += 1
            
        return head
# @lc code=end