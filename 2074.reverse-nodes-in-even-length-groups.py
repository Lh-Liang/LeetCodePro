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
        # The first group (size 1) is always odd and never reversed.
        # We start tracking from the node after the first group.
        prev = head
        k = 2
        
        while prev.next:
            # 1. Count the actual length of the current group
            curr = prev.next
            count = 0
            temp = curr
            while temp and count < k:
                temp = temp.next
                count += 1
            
            # 2. Check if the actual length is even
            if count % 2 == 0:
                # Reverse 'count' nodes starting from 'curr'
                # 'temp' is the node immediately after this group
                rev_prev = temp
                rev_curr = curr
                for _ in range(count):
                    nxt = rev_curr.next
                    rev_curr.next = rev_prev
                    rev_prev = rev_curr
                    rev_curr = nxt
                
                # Connect the node before the group to the new head of the reversed group
                prev.next = rev_prev
                # After reversal, 'curr' is now the tail of this group
                prev = curr
            else:
                # Actual length is odd, skip reversal
                # Move 'prev' to the end of the current group
                for _ in range(count):
                    prev = prev.next
            
            # Increment expected group size
            k += 1
            
        return head
# @lc code=end