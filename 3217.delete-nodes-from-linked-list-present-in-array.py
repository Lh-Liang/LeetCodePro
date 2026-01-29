#
# @lc app=leetcode id=3217 lang=python3
#
# [3217] Delete Nodes From Linked List Present in Array
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) lookups
        num_set = set(nums)
        
        # Create a dummy node that points to head
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize pointers
        current = head
        prev = dummy
        
        # Traverse the linked list
        while current:
            if current.val in num_set:
                # Remove current node by linking previous node's next to current's next
                prev.next = current.next
            else:
                # Move prev pointer only when no deletion occurs
                prev = current
            # Move to next node
            current = current.next
        
        return dummy.next  # Return new head skipping dummy node