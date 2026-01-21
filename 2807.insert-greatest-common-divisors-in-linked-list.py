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
        # If the list has 0 or 1 node, no pairs exist to insert GCDs
        if not head or not head.next:
            return head
        
        curr = head
        # Iterate through the list as long as there is a pair of nodes
        while curr and curr.next:
            # Calculate GCD of current node and next node values
            gcd_val = math.gcd(curr.val, curr.next.val)
            
            # Create the new node with the GCD value
            new_node = ListNode(gcd_val)
            
            # Insert the new node between curr and curr.next
            new_node.next = curr.next
            curr.next = new_node
            
            # Move curr to the node that was originally next
            # (now it's two steps ahead: curr -> new_node -> original_next)
            curr = new_node.next
            
        return head
# @lc code=end