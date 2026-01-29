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
        def reverse_ll(curr):
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        if not head:
            return None
        
        rev = reverse_ll(head)
        cur = rev
        carry = 0
        tail = None
        while cur:
            total = cur.val * 2 + carry
            cur.val = total % 10
            carry = total // 10
            tail = cur
            cur = cur.next
        if carry:
            tail.next = ListNode(carry)
        return reverse_ll(rev)

# @lc code=end