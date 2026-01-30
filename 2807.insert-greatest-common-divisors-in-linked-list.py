#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
from typing import Optional, List
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # No pairs to process if less than two nodes.
        current = head
        while current and current.next:
            gcd_value = math.gcd(current.val, current.next.val)  # Calculate GCD of current pair.
            new_node = ListNode(val=gcd_value)  # Create new node with GCD value.
            new_node.next = current.next  # Link new node to next node in list.
            current.next = new_node  # Link current node to new node.
            current = new_node.next  # Move to next pair in list.
        return head  # Return modified list with inserted GCDs.
# @lc code=end