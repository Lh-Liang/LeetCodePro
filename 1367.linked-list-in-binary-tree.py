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
        # Check if the path starts at the current root node
        if self.checkPath(head, root):
            return True
        # Otherwise, check recursively in left and right subtrees
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def checkPath(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        # If we successfully traversed the whole list, return True
        if not head:
            return True
        # If we hit a null node in the tree but haven't finished the list, return False
        if not node:
            return False
        # If values don't match, return False
        if head.val != node.val:
            return False
        # Continue checking the next list node in both left and right children
        return self.checkPath(head.next, node.left) or self.checkPath(head.next, node.right)
# @lc code=end