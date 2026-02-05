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
    def reverseEvenLengthGroups(self, head: ListNode) -> ListNode:
        # Function to reverse a segment of linked list given start and end nodes
        def reverse_segment(start, end):
            prev, current = None, start
            while current != end:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            return prev  # New head of this reversed section is returned
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy  # End of previous processed group initially set before head
        group_length = 1  # Start with first group length as per problem statement
        
        while head:
            count = 0  # To count actual number of nodes in this group (may differ for last group)
            tail = head  # Tail will point to last node in this group after counting them out.
            for _ in range(group_length):
                if not tail:
                    break
                count += 1
                tail = tail.next
            
            if count % 2 == 0:
                # If count (group length) is even, we need to reverse this segment from head to tail (exclusive)
                next_group_head = tail  # Next group starts from here after reversal.
                new_head_of_reversed_segment = reverse_segment(head, tail)
                prev_group_end.next = new_head_of_reversed_segment
                head.next = next_group_head 
                prev_group_end = head 
            else:
                # If odd, just link previous group's end to current group's start without reversal.
                prev_group_end.next = head 
                prev_group_end = tail if tail else head 
            
            # Move `head` pointer to where next group's first node would be (tail currently)
            head = tail 
            group_length += 1 
        return dummy.next  # Return actual new head after all operations are complete.
# @lc code=end