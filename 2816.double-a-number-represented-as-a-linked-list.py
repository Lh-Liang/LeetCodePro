#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the head value is 5 or more, doubling it will result in a carry
        # that creates a new most-significant digit (e.g., 50 -> 100).
        if head.val >= 5:
            head = ListNode(0, head)

        curr = head
        while curr:
            # The new value for the current node is the units digit of (val * 2).
            # Note: (val * 2) % 10 is always between 0 and 8 for val in [0, 9].
            curr.val = (curr.val * 2) % 10
            
            # A carry is added if the next node's value is 5 or more.
            # We check the original value of next before it gets doubled.
            if curr.next and curr.next.val >= 5:
                curr.val += 1
            
            curr = curr.next
            
        return head
# @lc code=end