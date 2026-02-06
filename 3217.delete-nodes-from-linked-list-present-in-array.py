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
        nums_set = set(nums)  # Step 1: Convert nums array to set for O(1) lookups.
        dummy = ListNode(0)  # Step 2: Initialize a dummy node to simplify edge case handling.
        dummy.next = head
        prev, current = dummy, head # Step 3: Traverse with two pointers (prev and current). 
        while current:
            if current.val in nums_set:
                prev.next = current.next # Bypass nodes with values in nums_set. 
            else:
                prev = current 
            current = current.next 
        return dummy.next # Step 4: Return modified list starting from next of dummy node.