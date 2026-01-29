#
# @lc app=leetcode id=2074 lang=python3
#
# [2074] Reverse Nodes in Even Length Groups
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev_tail = head
        k = 2
        
        while prev_tail.next:
            # Count actual nodes in the current group
            n = 0
            curr = prev_tail.next
            while curr and n < k:
                curr = curr.next
                n += 1
            
            if n % 2 == 0:
                # Reverse the current group of size n
                group_start = prev_tail.next
                rev_prev = None
                curr = group_start
                for _ in range(n):
                    nxt = curr.next
                    curr.next = rev_prev
                    rev_prev = curr
                    curr = nxt
                
                # Connect the reversed segment back into the list
                prev_tail.next = rev_prev
                group_start.next = curr
                prev_tail = group_start
            else:
                # Skip the current group of size n
                for _ in range(n):
                    prev_tail = prev_tail.next
            
            k += 1
            
        return head
# @lc code=end