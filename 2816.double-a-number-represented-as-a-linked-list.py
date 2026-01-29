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
        # If the head value is 5 or more, doubling it will cause a carry.
        # We handle this by prepending a node with value 0 which will then be updated.
        if head.val >= 5:
            head = ListNode(0, head)
        
        curr = head
        while curr:
            # Update current node's value based on its doubling.
            # The modulo 10 handles the digit, and we look ahead to handle the carry.
            val = (curr.val * 2) % 10
            
            # If the next node exists and its original value is >= 5, 
            # it will generate a carry for the current node.
            if curr.next and curr.next.val >= 5:
                val += 1
            
            curr.val = val
            curr = curr.next
            
        return head
# @lc code=end