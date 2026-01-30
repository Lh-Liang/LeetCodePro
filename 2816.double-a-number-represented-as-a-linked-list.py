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
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        head = reverse(head)
        curr = head
        carry = 0
        prev = None
        while curr:
            total = curr.val * 2 + carry
            curr.val = total % 10
            carry = total // 10
            prev = curr
            curr = curr.next
        if carry:
            prev.next = ListNode(carry)
        return reverse(head)
# @lc code=end