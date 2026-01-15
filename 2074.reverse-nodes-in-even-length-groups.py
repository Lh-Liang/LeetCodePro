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
        if not head:
            return head
        # We'll process groups one by one
        # Use a dummy node to simplify handling of the head
        dummy = ListNode(0, head)
        prev_group_end = dummy  # points to the node before the current group start
        current_group_len = 1  # length of the current group we are trying to form (1-indexed)
        
        while True:
            # Determine the actual length of this group (might be less if we reach end)
            # We need to count how many nodes are available for this group
            count = 0
            walk = prev_group_end.next  # start of current group
            # Count nodes until we have current_group_len nodes or reach end
            while walk and count < current_group_len:
                walk = walk.next
                count += 1
            # Now count is the number of nodes in this group (could be less than desired)
            if count == 0:
                break  # no more nodes left, should not happen because we break when walk becomes None but we handle later.
            
            # If count is even, we need to reverse this group.
            if count % 2 == 0:
                # Reverse the group of size count.
                # prev_group_end.next is the first node of the group.
                group_start = prev_group_end.next
                # We'll reverse count nodes starting from group_start.
                prev = None
                cur = group_start
                for _ in range(count):
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
                # After reversal, prev is the new head of the reversed group (i.e., last node becomes first)
                new_group_head = prev
                # The original group_start is now the tail of the reversed group.
                new_group_tail = group_start  # because after reversal, group_start becomes tail (since it was first)
                # Connect previous part to new head.
                prev_group_end.next = new_group_head
                # Connect tail to the next part (cur is the node after the group).
                new_group_tail.next = cur
                # Update prev_group_end for next iteration: should be new_group_tail (which is now at end of this group).
                prev_group_end = new_group_tail
            else:
                # Group length is odd, just skip over these nodes without reversal.
                # Move prev_group_end forward by count nodes.
                for _ in range(count):
                    prev_group_end = prev_group_end.next
            
            current_group_len += 1  # next group length increases by 1.
        
        return dummy.next