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
        def helper(node):
            if not node:
                return 0
            
            carry = helper(node.next)
            doubled = node.val * 2 + carry
            node.val = doubled % 10
            return doubled // 10
        
        carry = helper(head)
        if carry:
            new_head = ListNode(carry)
            new_head.next = head
            return new_head
        return head
# @lc code=end