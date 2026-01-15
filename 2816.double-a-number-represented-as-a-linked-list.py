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
        # Helper function to reverse linked list
        def reverse(head):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        # Step 1: Reverse list so least significant digit is head
        rev_head = reverse(head)
        
        # Step 2: Double each digit with carry
        carry = 0
        cur = rev_head
        tail = None
        while cur:
            total = cur.val * 2 + carry
            cur.val = total % 10
            carry = total // 10
            if not cur.next:
                tail = cur
            cur = cur.next
        
        # Step 3: Add new node if carry remains
        if carry:
            tail.next = ListNode(carry)
        
        # Step 4: Reverse back and return
        return reverse(rev_head)
# @lc code=end