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
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        head = reverse(head)

        carry = 0
        cur = head
        prev = None
        while cur:
            total = cur.val * 2 + carry
            cur.val = total % 10
            carry = total // 10
            prev = cur
            cur = cur.next

        if carry:
            prev.next = ListNode(carry)

        head = reverse(head)
        return head
# @lc code=end
