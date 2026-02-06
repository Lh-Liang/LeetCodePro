#
# @lc app=leetcode id=2074 lang=python3
#
# [2074] Reverse Nodes in Even Length Groups
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        current = head
        prev_group_end = None
        group_size = 1
        
        while current:
            # Determine the current group size
            count = 0
            start_of_group = current
            while current and count < group_size:
                current = current.next
                count += 1
            
            # Check if this is an even length group to reverse it
            if count % 2 == 0:
                # Reverse this section of nodes from start_of_group to current (exclusive)
                prev, curr = None, start_of_group
                for _ in range(count):
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node
                
                # Connect the reversed group with previous part of the list and upcoming part of the list. 
                if prev_group_end:
                    prev_group_end.next = prev  # prev now is the new start of this reversed group.
                else:
                    head = prev  # If we're reversing from the first node. 
                start_of_group.next = current  # Connect end of reversed group to upcoming nodes. 
                prev_group_end = start_of_group  # Move end marker to end of this reversed group. 	     	     	      	   	   	   	         	   	   	   	         else:	     	     # Move end marker forward if not reversed (odd length). 	         if prev_group_end:	       prev_group_end.next = start_of_group  # Connect last node with new starting point of next round (if any).     else:    head = start_of_group      prev_group_end=start_of_group     if not current: break # Reached end of list increase.group size for next round traverse .group_size +=1 return head