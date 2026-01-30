#
# @lc app=leetcode id=2074 lang=python3
#
# [2074] Reverse Nodes in Even Length Groups
#

# @lc code=start
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize variables for traversal and group tracking
        prev_tail = None  # Keeps track of the last node before current group
        current = head    # Current node for iteration
        group_size = 1    # Start with group size 1 as per problem statement
        
        while current:
            # Determine actual size of the current group
            count = 0  # To count nodes in current group
            node = current  # Start from current position for counting length
            while node and count < group_size:
                node = node.next
                count += 1
            
            # Reverse if count (group length) is even
            if count % 2 == 0:
                prev = None  # Previous node for reversal process
                temp_node = current  # Temporary node to traverse and reverse within group size limits
                for _ in range(count):
                    next_node = temp_node.next  # Store next node temporarily 
                    temp_node.next = prev       # Reverse link direction 
                    prev = temp_node            # Move previous up by one for next iteration 
                    temp_node = next_node       # Move to next actual node for processing/reversal 
                if prev_tail:
                    prev_tail.next = prev   # Connect last reversed part to previous segment's tail if exists 
                else:
                    head = prev             # If there's no previous segment, update head to new start point (first reversed)
                current.next = temp_node   # Connect last processed (start point) onward to next segment's start/unprocessed part 
            else:
                prev_tail = current         # Update tail tracker since this group's not reversed entirely 
                for _ in range(count - 1):
                    current = current.next   
                current = current.next if current else None   # Safely move forward or terminate processing loop by breaking out once fully traversed until end (None)	    			    								                  			     			       	      	          	   	          	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ⁞        Ɲ\u0003\u0003\u0003\u0003\u0003