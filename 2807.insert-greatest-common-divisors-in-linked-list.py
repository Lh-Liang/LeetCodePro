#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

import math

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        while current and current.next:
            gcd_value = math.gcd(current.val, current.next.val)
            new_node = ListNode(gcd_value)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        return head
# @lc code=end