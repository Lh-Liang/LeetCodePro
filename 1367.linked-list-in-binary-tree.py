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
        def checkPath(h, r):
            if not h:
                return True
            if not r:
                return False
            if h.val != r.val:
                return False
            return checkPath(h.next, r.left) or checkPath(h.next, r.right)
        
        if not root:
            return False
        
        # Use iterative DFS to traverse the tree and find the start of the path
        stack = [root]
        while stack:
            curr = stack.pop()
            # Check if the list starts at the current tree node
            if checkPath(head, curr):
                return True
            # Add children to the stack to continue searching the tree
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
        return False
# @lc code=end