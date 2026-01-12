#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # Check if the list starts at the current root, or search in left/right subtrees
        return self.checkPath(head, root) or \
               self.isSubPath(head, root.left) or \
               self.isSubPath(head, root.right)

    def checkPath(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        # If we reached the end of the linked list, we found a match
        if not head:
            return True
        # If the tree ends but the list hasn't, no match
        if not node:
            return False
        # If values don't match, this path is invalid
        if head.val != node.val:
            return False
        
        # Current values match, continue checking the next list node in both child paths
        return self.checkPath(head.next, node.left) or \
               self.checkPath(head.next, node.right)
# @lc code=end