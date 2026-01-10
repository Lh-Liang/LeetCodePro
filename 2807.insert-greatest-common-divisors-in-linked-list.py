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
            # Calculate GCD of current node and next node
            gcd_val = math.gcd(curr.val, curr.next.val)
            
            # Create the new node to insert
            new_node = ListNode(gcd_val)
            
            # Insert the new node: curr -> new_node -> curr.next
            new_node.next = curr.next
            curr.next = new_node
            
            # Move curr to the next original node (skip the inserted node)
            curr = new_node.next
            
        return head
# @lc code=end