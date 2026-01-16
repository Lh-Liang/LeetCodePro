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
        
        # Start with group size 1
        group_size = 1
        prev_group_end = None
        current = head
        
        while current:
            # Count actual nodes in current group
            count = 0
            temp = current
            while temp and count < group_size:
                temp = temp.next
                count += 1
            
            # If group has even length, reverse it
            if count % 2 == 0:
                # Reverse nodes from current to current + count - 1
                prev = temp  # This will be the next node after the group
                group_start = current
                
                # Reverse count nodes starting from current
                for _ in range(count):
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                
                # Connect previous group to reversed group
                if prev_group_end:
                    prev_group_end.next = prev
                else:
                    # If this is the first group, update head
                    head = prev
                
                # Update prev_group_end to the end of current reversed group (which was the start before reversal)
                prev_group_end = group_start
            else:
                # Odd length group - no reversal needed
                # Just move prev_group_end to the end of this group and advance current
                for _ in range(count):
                    if prev_group_end:
                        prev_group_end = prev_group_end.next
                    current = current.next
                
                # If this is the first group and it's odd, head remains unchanged but we set prev_group_end 
                if not prev_group_end:
                    prev_group_end = head if head else None 
                    temp_node = head 
                    for _ in range(count - 1): 
                        if temp_node: 
                            temp_node = temp_node.next 
                    if temp_node: 
                        prev_group_end = temp_node 
                    
            # Increase group size for next iteration    
            group_size += 1 
            
        return head 
# @lc code=end