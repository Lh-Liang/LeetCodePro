#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
from math import gcd
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional['ListNode']) -> Optional['ListNode']:
        cur = head
        while cur and cur.next:
            nxt = cur.next
            g = gcd(cur.val, nxt.val)
            cur.next = ListNode(g, nxt)
            cur = nxt
        return head
# @lc code=end
