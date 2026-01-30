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
        current = head
        previous_group_end = None  # To connect with reversed groups later
        group_length = 1  # Start with first group length as 1
        
        while current:
            # Determine actual group size
            count = 0
            temp = current
            while count < group_length and temp:
                temp = temp.next
                count += 1
            
            if count % 2 == 0:  # Even length, we need to reverse this group
                prev = None
                tail_of_current_group = current  # This will become end after reversal
                for _ in range(count):
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                
                # Connect last group's end to reversed start if it exists otherwise update head if it's first reverse operation.
                if previous_group_end:
                    previous_group_end.next = prev
                else:
                    head = prev  # New head if reversing first full-length even group starting at original head.
                
                tail_of_current_group.next = current  # Connect reversed group's end to rest of list or None.
                previous_group_end = tail_of_current_group  # Update last processed node (end of reversed section)
            else:
                # Just skip over this non-reversed section by iterating through it directly.
                previous_group_end = current if not previous_group_end else previous_group_end.next 
                for _ in range(count):
                    previous_group_end = current  # Move previous group's end pointer up without reversals here.
                    current = current.next          
            
            # Increase intended length for next possible even-length check group.
            group_length += 1      
        return head