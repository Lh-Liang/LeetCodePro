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
        
        # The first group is always size 1 (odd), so we start with the second group.
        prev = head
        group_size = 2
        
        while prev.next:
            # Count actual nodes in the current group
            curr = prev.next
            count = 0
            while count < group_size and curr:
                curr = curr.next
                count += 1
            
            if count % 2 == 0:
                # Reverse the nodes in this group
                curr = prev.next
                rev_prev = None
                for _ in range(count):
                    nxt = curr.next
                    curr.next = rev_prev
                    rev_prev = curr
                    curr = nxt
                
                # Re-link the reversed group back into the list
                # tail is the original first node, which is now the last node of the group
                tail = prev.next
                prev.next = rev_prev
                tail.next = curr
                prev = tail
            else:
                # If the group size is odd, just skip it
                for _ in range(count):
                    prev = prev.next
            
            # Increment expected group size for the next iteration
            group_size += 1
            
        return head
# @lc code=end