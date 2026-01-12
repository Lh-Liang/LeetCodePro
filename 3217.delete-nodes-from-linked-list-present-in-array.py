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
        # Convert nums to a set for O(1) average lookup time
        lookup = set(nums)
        
        # Use a dummy node to simplify edge cases where the head is removed
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Iterate through the list
        while current.next:
            if current.next.val in lookup:
                # Skip the node if its value is in the lookup set
                current.next = current.next.next
            else:
                # Move to the next node if the value is not in the set
                current = current.next
        
        return dummy.next
# @lc code=end