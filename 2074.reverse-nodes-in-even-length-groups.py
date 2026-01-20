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
        # The first group always has length 1 (odd), so head never changes.
        # We can start processing from the second group.
        
        prev_group_tail = head
        target_len = 2
        
        while prev_group_tail and prev_group_tail.next:
            # Step 1: Count actual number of nodes in the current group
            curr = prev_group_tail.next
            count = 0
            # We need to traverse to find the length, but keep a pointer to the end of this group
            # to easily link if we don't reverse.
            temp = curr
            while count < target_len and temp:
                temp = temp.next
                count += 1
            
            # Step 2: Determine if we reverse
            if count % 2 == 0:
                # Reverse 'count' nodes starting from prev_group_tail.next
                
                # Standard linked list reversal for specific length
                # We are reversing nodes from `cur` to the node before `temp`
                reverse_prev = None
                reverse_curr = curr
                nextNode = None
                
                for _ in range(count):
                    nextNode = reverse_curr.next
                    reverse_curr.next = reverse_prev
                    reverse_prev = reverse_curr
                    reverse_curr = nextNode
                
                # Now `reverse_prev` is the new head of this reversed group
                # `curr` is the new tail of this reversed group
                # `reverse_curr` (or `nextNode`) is the node coming after this group
                
                # Connect the previous part of the list to the new head
                prev_group_tail.next = reverse_prev
                # Connect the new tail to the rest of the list
                curr.next = reverse_curr
                
                # Update prev_group_tail for the next iteration
                # The new tail is `curr`
                prev_group_tail = curr
                
            else:
                # Length is odd, just move prev_group_tail forward by count
                for _ in range(count):
                    prev_group_tail = prev_group_tail.next
            
            target_len += 1
            
        return head
# @lc code=end