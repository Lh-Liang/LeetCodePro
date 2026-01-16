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
        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_temp = current.next
                current.next = prev
                prev = current
                current = next_temp
            return prev
        
        # Reverse the list to process from least significant digit
        reversed_head = reverse_list(head)
        
        # Process each digit, doubling and handling carry
        current = reversed_head
        carry = 0
        
        while current:
            doubled = current.val * 2 + carry
            current.val = doubled % 10
            carry = doubled // 10
            
            # If we're at the last node and there's still carry, we need a new node
            if not current.next and carry > 0:
                current.next = ListNode(0)
            
            current = current.next
        
        # Reverse back to get the final result
        return reverse_list(reversed_head)
# @lc code=end