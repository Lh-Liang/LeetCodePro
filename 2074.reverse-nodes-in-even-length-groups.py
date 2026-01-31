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
        # The first group always has length 1 (odd), so it's never reversed.
        # We start with the second group (expected size 2).
        prev_group_end = head
        expected_group_size = 2
        
        while prev_group_end.next:
            # Count actual nodes in the current group
            node = prev_group_end.next
            actual_size = 0
            while node and actual_size < expected_group_size:
                actual_size += 1
                node = node.next
            
            if actual_size % 2 == 0:
                # Reverse the nodes in this group
                curr = prev_group_end.next
                prev = None
                for _ in range(actual_size):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                
                # Connect the reversed segment back to the list
                # prev is the new head of the group, curr is the node after the group
                group_tail = prev_group_end.next
                group_tail.next = curr
                prev_group_end.next = prev
                
                # Move pointer to the end of this group
                prev_group_end = group_tail
            else:
                # Skip the nodes in this group
                for _ in range(actual_size):
                    prev_group_end = prev_group_end.next
            
            expected_group_size += 1
            
        return head
# @lc code=end