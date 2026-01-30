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
from typing import List, Optional
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)  # Convert list to set for O(1) lookups.
        dummy = ListNode(0)  # Dummy node to handle edge cases.
        dummy.next = head
        current = dummy
        while current.next:  # Traverse the linked list.
            if current.next.val in nums_set:
                current.next = current.next.next  # Skip nodes with values in nums_set.
            else:
                current = current.next  # Move to next node otherwise.
        return dummy.next  # Return the head of the modified list.
# @lc code=end