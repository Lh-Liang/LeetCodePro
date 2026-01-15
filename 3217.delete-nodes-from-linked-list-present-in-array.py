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
        nums_set = set(nums)
        # Create a dummy node to simplify removal of head if needed
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr:
            if curr.val in nums_set:
                # Skip current node
                prev.next = curr.next
                # Move current to next node, prev stays the same
                curr = curr.next
            else:
                # Keep current node, move both pointers
                prev = curr
                curr = curr.next
        
        return dummy.next
# @lc code=end