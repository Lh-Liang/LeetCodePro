#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize carry variable
        carry = 0
        current = head
        prev = None
        
        # Step 2-5: Traverse and process each node in the list
        while current is not None:
            # Step 3: Calculate new value with carry
            new_value = (current.val * 2) + carry
            
            # Step 4: Update current node's value and carry
            current.val = new_value % 10
            carry = new_value // 10
            
            # Step 5: Move to the next node, keep track of previous node for adding extra node if needed.
            prev = current
            current = current.next
        
        # Step 6: If there's any remaining carry, add it as a new node at the end.
        if carry > 0:
            prev.next = ListNode(carry)
        
        return head
# @lc code=end