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
        
        # Try starting the match from the current root, or search in subtrees
        if self.checkPath(head, root):
            return True
            
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def checkPath(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        # If we reached the end of the list, we found a valid path
        if not head:
            return True
        # If we reached a leaf in the tree before the end of the list
        if not node:
            return False
        # If values don't match, this specific path is invalid
        if head.val != node.val:
            return False
        
        # Continue matching the next list node in the tree's children
        return self.checkPath(head.next, node.left) or self.checkPath(head.next, node.right)
# @lc code=end