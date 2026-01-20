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
        def reverse_ll(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        
        rev = reverse_ll(head)
        cur = rev
        carry = 0
        tail = None
        while cur:
            val = cur.val * 2 + carry
            cur.val = val % 10
            carry = val // 10
            tail = cur
            cur = cur.next
        if carry:
            tail.next = ListNode(carry)
        return reverse_ll(rev)
        
# @lc code=end