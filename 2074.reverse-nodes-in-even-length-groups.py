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
        
        # The first group always has length 1, which is odd, so it's never reversed.
        # We start tracking from the second group (expected length 2).
        prev_group_tail = head
        curr = head.next
        expected_group_len = 2
        
        while curr:
            # Count actual nodes available in the current group
            temp = curr
            actual_len = 0
            while actual_len < expected_group_len and temp:
                temp = temp.next
                actual_len += 1
            
            if actual_len % 2 == 0:
                # Reverse this group of actual_len nodes
                # temp is the start of the next group
                rev_prev = temp
                rev_curr = curr
                for _ in range(actual_len):
                    rev_next = rev_curr.next
                    rev_curr.next = rev_prev
                    rev_prev = rev_curr
                    rev_curr = rev_next
                
                # Connect previous group's tail to the new head of this reversed group
                prev_group_tail.next = rev_prev
                # The original start of the group (curr) is now the tail of the reversed group
                prev_group_tail = curr
                # Move curr to the start of the next group
                curr = temp
            else:
                # If the group length is odd, skip reversal and move pointers forward
                for _ in range(actual_len):
                    prev_group_tail = curr
                    curr = curr.next
            
            expected_group_len += 1
            
        return head
# @lc code=end