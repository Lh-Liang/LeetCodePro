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
        nums_set = set(nums)  # Convert array to set for O(1) lookups
        dummy = ListNode(0)  # Dummy node to handle edge cases easily
        dummy.next = head  # Point dummy node to head of the list
        current = dummy  # Start with the dummy node
        
        while current.next is not None:
            if current.next.val in nums_set:
                # Skip over nodes with values in nums_set
                current.next = current.next.next
            else:
                # Move to next node if it's not being removed
                current = current.next
        
        return dummy.next  # Return head of modified list which is dummy's next pointer
# @lc code=end