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
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        group_size = 1
        while curr:
            # Find the length of this group
            group_head = curr
            count = 0
            temp = curr
            while temp and count < group_size:
                temp = temp.next
                count += 1
            # If even, reverse the group
            if count % 2 == 0:
                prev_next = prev.next
                prev_sub = prev
                curr_sub = curr
                prev_node = None
                for _ in range(count):
                    next_node = curr_sub.next
                    curr_sub.next = prev_node
                    prev_node = curr_sub
                    curr_sub = next_node
                prev.next = prev_node
                prev_next.next = curr_sub
                prev = prev_next
                curr = curr_sub
            else:
                # Move prev to the last node of this group
                for _ in range(count):
                    prev = curr
                    curr = curr.next
            # Verification: ensure all pointers are correctly updated and no nodes are lost
            # (Implicit in traversal and reconnection logic)
            group_size += 1
        # Verification: at end, all nodes should be present and linked correctly
        return dummy.next
# @lc code=end