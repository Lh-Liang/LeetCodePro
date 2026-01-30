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
        if not head:
            return None
        dummy = ListNode(0)
        prev = dummy
        current = head
        carry = 0
        while current:
            total = current.val * 2 + carry
            current.val = total % 10
            carry = total // 10
            prev.next = current
            prev = current
            current = current.next
        if carry > 0:
            prev.next = ListNode(carry)
        return dummy.next # @lc code=end