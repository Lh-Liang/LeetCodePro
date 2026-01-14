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
        def dfs(head, root):
            # If we've matched the entire linked list
            if not head:
                return True
            # If tree is exhausted but list isn't
            if not root:
                return False
            # Values must match, then continue down either left or right child
            return head.val == root.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        
        if not root:
            return False
        
        # Try matching from current root, or try starting from left/right subtrees
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
# @lc code=end