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
        
        def checkPath(head_node, tree_node):
            if not head_node:
                return True
            if not tree_node:
                return False
            if head_node.val != tree_node.val:
                return False
            return checkPath(head_node.next, tree_node.left) or checkPath(head_node.next, tree_node.right)
        
        if checkPath(head, root):
            return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
# @lc code=end