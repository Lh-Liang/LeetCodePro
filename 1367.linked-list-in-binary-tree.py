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
        def dfs(node, lnode):
            if not lnode:
                return True
            if not node or node.val != lnode.val:
                return False
            return dfs(node.left, lnode.next) or dfs(node.right, lnode.next)
        
        def traverse(node):
            if not node:
                return False
            if node.val == head.val and dfs(node, head):
                return True
            return traverse(node.left) or traverse(node.right)
        
        return traverse(root)
# @lc code=end