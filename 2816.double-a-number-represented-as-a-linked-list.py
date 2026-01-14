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
        # Create a dummy node to handle potential overflow at the head
        dummy = ListNode(0, head)
        
        curr = dummy
        while curr:
            # Double the current value
            doubled = curr.val * 2
            # Add 1 if the next node will produce a carry (next.val >= 5)
            if curr.next and curr.next.val >= 5:
                doubled += 1
            curr.val = doubled % 10
            curr = curr.next
        
        # Return dummy if it has a non-zero value, otherwise skip it
        return dummy if dummy.val != 0 else dummy.next
# @lc code=end