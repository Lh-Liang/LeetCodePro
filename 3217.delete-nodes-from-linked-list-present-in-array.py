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
        # Convert nums to a set for O(1) lookup
        lookup = set(nums)
        
        # Use a dummy node to handle cases where the head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next:
            if curr.next.val in lookup:
                # Skip the node by pointing to the one after it
                curr.next = curr.next.next
            else:
                # Only move the pointer forward if we didn't delete a node
                curr = curr.next
                
        return dummy.next
# @lc code=end