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
        nums_set = set(nums)  # Convert nums array to set for O(1) lookups
        dummy = ListNode(0)  # Create a dummy node to handle edge cases easily
        dummy.next = head
        prev = dummy  # Initialize prev as dummy node
        current = head  # Start with the head of the linked list
        while current:
            if current.val in nums_set:  # If current node's value is in nums_set
                prev.next = current.next  # Skip the current node by linking prev to current's next
            else:
                prev = current  # Move prev pointer forward only if we didn't remove current node
            current = current.next  # Move to next node in the list
        return dummy.next  # Return the modified list starting from dummy's next node
# @lc code=end