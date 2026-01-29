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
        current = head
        prev_tail = None
        group_length = 1
        while current:
            # Determine the actual size of this group
            count = 0
            start_node = current
            while count < group_length and current:
                current = current.next
                count += 1
            if count % 2 == 0: # Reverse this even-length group
                prev_node = None
                tail_node = start_node # This will become new tail after reversal.
                for _ in range(count):
                    next_node = start_node.next 
                    start_node.next = prev_node 
                    prev_node = start_node 
                    start_node = next_node 
                # Link previous group's tail to new head after reversal.
                if prev_tail:
                    prev_tail.next = prev_node 
                else:
                    head = prev_node # New head if first node was part of even-length reversal.
                tail_node.next = current # Connect reversed part back to remaining list.
                prev_tail = tail_node # Update previous group's tail reference.
            else:
                # Just update reference without reversing because length is odd.
                if prev_tail:
                    prev_tail.next = start_node 
                prev_tail = None if count == 0 else prev_tail or start_node 
            # Prepare for next iteration/group with increasing length.
            group_length += 1 
        return head
# @lc code=end