#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
from math import gcd
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            next_node = current.next
            gcd_value = gcd(current.val, next_node.val)
            gcd_node = ListNode(val=gcd_value)
            current.next = gcd_node
            gcd_node.next = next_node
            current = next_node
        return head
# @lc code=end