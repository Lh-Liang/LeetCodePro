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
        # or if it exists in the left or right subtrees.
        return self.checkPath(head, root) or \
               self.isSubPath(head, root.left) or \
               self.isSubPath(head, root.right)

    def checkPath(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        # If we reached the end of the list, we found the path.
        if not head:
            return True
        # If we reached the end of the tree path before the list, no match.
        if not node:
            return False
        # If values do not match, this specific path is not a subpath.
        if head.val != node.val:
            return False
        
        # Continue checking the next node in the list in either the left or right child.
        return self.checkPath(head.next, node.left) or self.checkPath(head.next, node.right)

# @lc code=end