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
        def dfs(tree, list_node):
            if list_node is None:
                return True
            if tree is None:
                return False
            if tree.val != list_node.val:
                return False
            return dfs(tree.left, list_node.next) or dfs(tree.right, list_node.next)

        def traverse(tree):
            if tree is None:
                return False
            if dfs(tree, head):
                return True
            return traverse(tree.left) or traverse(tree.right)

        return traverse(root)
# @lc code=end