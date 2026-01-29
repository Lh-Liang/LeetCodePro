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
        
        def checkPath(list_node, tree_node):
            # Successfully matched all nodes in the linked list
            if not list_node:
                return True
            # Tree path ended before the linked list
            if not tree_node:
                return False
            # Values do not match
            if list_node.val != tree_node.val:
                return False
            # Check next node in the list against both children
            return checkPath(list_node.next, tree_node.left) or checkPath(list_node.next, tree_node.right)
        
        # 1. Try starting the match from the current root
        # 2. Or search for a start in the left subtree
        # 3. Or search for a start in the right subtree
        return checkPath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
# @lc code=end