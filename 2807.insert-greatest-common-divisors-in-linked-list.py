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
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            gcd_val = math.gcd(curr.val, curr.next.val)
            new_node = ListNode(gcd_val, curr.next)
            curr.next = new_node
            curr = new_node.next
        # Verification step: Ensure list integrity
        # ptr = head
        # seen = set()
        # while ptr:
        #     assert ptr not in seen, "Cycle detected in linked list."
        #     seen.add(ptr)
        #     ptr = ptr.next
        return head
# @lc code=end