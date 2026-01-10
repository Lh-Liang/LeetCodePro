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
        # If the leading digit is 5 or greater, doubling will result in an extra digit.
        # We can prepend a 0 node to handle the carry logic uniformly.
        if head.val >= 5:
            head = ListNode(0, head)
        
        curr = head
        while curr:
            # Double the current value and keep only the units digit
            curr.val = (curr.val * 2) % 10
            
            # If the next node exists and its value is 5 or more, 
            # it will produce a carry of 1 for the current node.
            if curr.next and curr.next.val >= 5:
                curr.val += 1
            
            curr = curr.next
            
        return head
# @lc code=end