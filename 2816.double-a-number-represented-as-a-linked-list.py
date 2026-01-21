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
        # If the head value is 5 or more, the result will have an extra digit at the front.
        if head.val >= 5:
            head = ListNode(0, head)
        
        curr = head
        while curr:
            # Update the current node's value: double it and take the last digit.
            # The maximum value of (val * 2) % 10 is 8.
            curr.val = (curr.val * 2) % 10
            
            # If the next node's original value is 5 or more, it will produce a carry.
            if curr.next and curr.next.val >= 5:
                curr.val += 1
            
            curr = curr.next
            
        return head
# @lc code=end