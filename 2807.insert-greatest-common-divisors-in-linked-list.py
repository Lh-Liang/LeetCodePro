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
        # Boundary condition: if list is empty or has only one node, no pairs exist
        if not head or not head.next:
            return head
        
        curr = head
        # Iterate through the list as long as there is a pair of nodes
        while curr and curr.next:
            # Calculate GCD using the math library
            gcd_val = math.gcd(curr.val, curr.next.val)
            
            # Create the new node to be inserted
            new_node = ListNode(gcd_val)
            
            # Insert new_node between curr and curr.next
            new_node.next = curr.next
            curr.next = new_node
            
            # Move curr to the node that was originally next to process the next pair
            curr = new_node.next
            
        return head
# @lc code=end