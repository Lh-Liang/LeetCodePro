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
        # Initialize current node pointer and carry.
        current = head
        carry = 0
        # Placeholder for the new head in case we have an additional digit.
        dummy_head = ListNode(0)
        prev = dummy_head
        # Traverse the list.
        while current is not None:
            # Calculate new value for current node.
            new_val = current.val * 2 + carry
            # Update carry for next node.
            carry = new_val // 10
            # Update current node's value to new value modulo 10 (last digit).
            prev.next = ListNode(new_val % 10)
            # Move pointers forward.
            prev = prev.next
            current = current.next
        # If there's any remaining carry after processing all nodes, create a new node.
        if carry > 0:
            prev.next = ListNode(carry)
        # Return updated list starting from dummy head's next pointer since dummy head is an extra node added initially.
        return dummy_head.next
# @lc code=end