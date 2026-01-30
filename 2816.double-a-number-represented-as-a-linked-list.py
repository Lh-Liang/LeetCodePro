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
        # Helper to reverse a linked list
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        head = reverse(head)
        curr = head
        carry = 0
        prev = None
        while curr:
            sum_ = curr.val * 2 + carry
            curr.val = sum_ % 10
            carry = sum_ // 10
            prev = curr
            curr = curr.next
        if carry:
            prev.next = ListNode(carry)
        return reverse(head)
# @lc code=end