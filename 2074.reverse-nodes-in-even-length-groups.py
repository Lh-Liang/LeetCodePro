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
        def reverse(start: ListNode, end: ListNode) -> ListNode:
            prev = None
            current = start
            while current != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        prev_group_end = None  # To connect previous groups correctly after reversal.
        current_node = head  # Start with head node.
        group_number = 1  # We start with first group size as 1.
        
        while current_node:
            count = 0  # Reset node count for this group.
            group_start = current_node  # The start of this new group.
            temp_node = current_node  # To determine length of this current group.
            
            # Count nodes in this group until we reach its supposed size or end of list.
            while count < group_number and temp_node:
                temp_node = temp_node.next
                count += 1
            
            if count % 2 == 0:  # Reverse if even length found.
                new_start = reverse(group_start, temp_node)
                if prev_group_end:
                    prev_group_end.next = new_start  # Link previous group's end to new start after reversing.
                else:
                    head = new_start  # Update head if first segment is reversed.
                
                prev_group_end = group_start  # Original start becomes end due to reversal now correctly linked.
            else:
                prev_group_end = temp_node if temp_node else group_start   # Maintain linkage if not reversed.
            
            current_node = temp_node  # Move to next group's start.
            group_number += 1         # Increment group size for next iteration.
        
        return head  # Return modified list's head reference post-processing all groups correctly inline handled.
# @lc code=end