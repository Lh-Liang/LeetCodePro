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
        
        # Create a dummy node to handle head removal easily
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the list
        while current.next:
            if current.next.val in nums_set:
                # Skip the node if its value is in the set
                current.next = current.next.next
            else:
                # Move to the next node if the current one is kept
                current = current.next
                
        return dummy.next
# @lc code=end