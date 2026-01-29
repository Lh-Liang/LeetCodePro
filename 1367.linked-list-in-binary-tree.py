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
        
        # Check if the path starts from the current root node
        if self.checkPath(head, root):
            return True
        
        # If not, try to find the path starting from left or right children
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def checkPath(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        # Success: reached the end of the linked list
        if not head:
            return True
        # Failure: reached a leaf in the tree before the end of the list
        if not node:
            return False
        # Failure: values do not match
        if head.val != node.val:
            return False
        
        # Continue matching the next list node in the downward tree paths
        return self.checkPath(head.next, node.left) or self.checkPath(head.next, node.right)
# @lc code=end