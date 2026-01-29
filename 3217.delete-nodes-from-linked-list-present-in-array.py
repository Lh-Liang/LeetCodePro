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
        # Convert list to set for O(1) average lookup time
        lookup = set(nums)
        
        # Use dummy node to handle deletions at the head
        dummy = ListNode(0, head)
        curr = dummy
        
        while curr.next:
            if curr.next.val in lookup:
                # Skip the node
                curr.next = curr.next.next
            else:
                # Only move forward if we didn't delete a node,
                # because the new curr.next needs to be checked.
                curr = curr.next
        
        return dummy.next
# @lc code=end