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
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        group_size = 1
        
        while prev_group_tail.next:
            # Count the actual number of nodes in this group
            actual_count = 0
            current = prev_group_tail.next
            while actual_count < group_size and current:
                actual_count += 1
                current = current.next
            
            if actual_count % 2 == 0:  # Even length group, need to reverse
                # Reverse 'actual_count' nodes starting from prev_group_tail.next
                curr = prev_group_tail.next
                first_node = curr  # Will become the tail after reversal
                prev_node = None
                
                for _ in range(actual_count):
                    next_node = curr.next
                    curr.next = prev_node
                    prev_node = curr
                    curr = next_node
                
                # Reconnect: prev_node is now the new head, curr is the next group's head
                prev_group_tail.next = prev_node
                first_node.next = curr
                prev_group_tail = first_node
            else:  # Odd length group, no reversal needed
                for _ in range(actual_count):
                    prev_group_tail = prev_group_tail.next
            
            group_size += 1
        
        return dummy.next
# @lc code=end