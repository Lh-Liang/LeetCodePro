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
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        prev = head
        while prev.next:
            curr = prev.next
            g = gcd(prev.val, curr.val)
            new_node = ListNode(g)
            new_node.next = curr
            prev.next = new_node
            prev = curr
        return head

# @lc code=end