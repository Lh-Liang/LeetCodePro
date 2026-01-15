#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from typing import Optional

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start from the head of the list
        curr = head
        # Traverse while there is a current node and a next node (pair exists)
        while curr and curr.next:
            # Compute the GCD of the current node and the next node's values
            gcd_val = math.gcd(curr.val, curr.next.val)
            # Create a new node with the GCD value, pointing to the original next node
            new_node = ListNode(gcd_val, curr.next)
            # Insert the new node after the current node
            curr.next = new_node
            # Move to the original next node (skip the newly inserted node)
            curr = new_node.next
        # Return the modified head (same as original head)
        return head
# @lc code=end