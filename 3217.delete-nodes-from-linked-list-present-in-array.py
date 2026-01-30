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
        remove_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            if curr.val in remove_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
# @lc code=end