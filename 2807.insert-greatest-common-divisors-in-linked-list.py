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
        if not head or not head.next:
            return head
        
        curr = head
        while curr and curr.next:
            # Calculate GCD of current and next node values
            gcd_val = math.gcd(curr.val, curr.next.val)
            
            # Create new node and insert it
            new_node = ListNode(val=gcd_val, next=curr.next)
            curr.next = new_node
            
            # Move curr to the node after the inserted GCD node
            curr = new_node.next
            
        return head
# @lc code=end