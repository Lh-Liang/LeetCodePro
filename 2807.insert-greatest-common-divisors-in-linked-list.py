#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
from math import gcd
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            # Get next node for calculation of gcd and insertion point.
            next_node = current.next
            # Calculate gcd of current value and next value.
            gcd_value = gcd(current.val, next_node.val)
            # Create a new node with this gcd value.
            gcd_node = ListNode(gcd_value) 
            # Link new node between current and next node. 
            current.next = gcd_node 
            gcd_node.next = next_node 
            # Move to next original node in sequence (skip over inserted node). 
            current = next_node 
        return head 
# @lc code=end