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
        # The first group always has length 1 (odd), so it is never reversed.
        # 'prev' tracks the node immediately preceding the current group.
        prev = head
        group_size = 2
        
        while prev.next:
            # 1. Count the actual number of nodes available for this group
            count = 0
            curr = prev.next
            while curr and count < group_size:
                count += 1
                curr = curr.next
            
            # 2. If the actual group length is even, reverse it
            if count % 2 == 0:
                node_to_reverse = prev.next
                rev_prev = None
                rev_curr = node_to_reverse
                
                # Standard in-place linked list reversal for 'count' nodes
                for _ in range(count):
                    next_node = rev_curr.next
                    rev_curr.next = rev_prev
                    rev_prev = rev_curr
                    rev_curr = next_node
                
                # 3. Reconnect the reversed segment
                # 'rev_prev' is the new head of the segment
                # 'rev_curr' is the first node of the next group
                # 'node_to_reverse' is the new tail of the segment
                tail = node_to_reverse
                prev.next = rev_prev
                tail.next = rev_curr
                
                # Move 'prev' to the tail of the processed group
                prev = tail
            else:
                # 4. If odd, skip reversal and move 'prev' to the last node of the group
                for _ in range(count):
                    prev = prev.next
            
            # Prepare for the next potential group
            group_size += 1
            
        return head
# @lc code=end