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
        def check_path(h, r):
            # If we reached the end of the linked list, it's a match
            if not h:
                return True
            # If we reached the end of a tree path but list isn't finished
            if not r:
                return False
            # If values don't match, this path is invalid
            if h.val != r.val:
                return False
            # Continue checking the rest of the list in child nodes
            return check_path(h.next, r.left) or check_path(h.next, r.right)
        
        if not root:
            return False
        
        # Try starting the match from the current root, or search in subtrees
        return check_path(head, root) or \
               self.isSubPath(head, root.left) or \
               self.isSubPath(head, root.right)
# @lc code=end