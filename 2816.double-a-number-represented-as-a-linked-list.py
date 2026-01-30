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
        current = head
        carry = 0
        while current is not None:
            current.val = current.val * 2 + carry
            if current.val >= 10:
                current.val -= 10
                carry = 1
            else:
                carry = 0
            if current.next is None: # If this is the last node and there is a carry, we need to add a new node.
                if carry == 1:
                    current.next = ListNode(1) # Adding new node with value of `carry` which should be `1` here.
                    break
            current = current.next # Move to next node in list.
        return head # Return modified head of list after processing all nodes. 
# @lc code=end