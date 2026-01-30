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
        def reverse(start, end):
            prev = end
            curr = start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        group_size = 1
        while curr:
            # Find the tail for this group
            tail = curr
            count = 1
            while count < group_size and tail.next:
                tail = tail.next
                count += 1
            next_group = tail.next
            if count % 2 == 0:
                # Reverse this group
                prev.next = reverse(curr, next_group)
                # After reversal, curr is the tail
                curr.next = next_group
                prev = curr
            else:
                prev = tail
            curr = next_group
            group_size += 1
        return dummy.next
# @lc code=end