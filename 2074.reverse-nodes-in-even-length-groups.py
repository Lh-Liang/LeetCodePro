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
        
        # The first group is always size 1 (odd), so we skip it.
        prev = head
        group_size = 2
        
        while prev.next:
            # 1. Count nodes in current group
            curr = prev.next
            actual_count = 0
            temp = curr
            while temp and actual_count < group_size:
                temp = temp.next
                actual_count += 1
            
            if actual_count % 2 == 0:
                # 2. Reverse even group
                rev_prev = None
                node = curr
                for _ in range(actual_count):
                    nxt = node.next
                    node.next = rev_prev
                    rev_prev = node
                    node = nxt
                
                # 3. Re-link
                # prev -> [reversed group] -> node (which is temp/next_start)
                prev.next = rev_prev
                curr.next = node
                prev = curr
            else:
                # 4. Skip odd group
                for _ in range(actual_count):
                    prev = prev.next
            
            group_size += 1
            
        return head
# @lc code=end