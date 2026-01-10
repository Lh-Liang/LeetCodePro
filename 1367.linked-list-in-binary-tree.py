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
        def check(h, r):
            # If we've reached the end of the linked list, we found a match
            if not h:
                return True
            # If the tree path ends before the linked list, no match
            if not r:
                return False
            # If values don't match, this path is invalid
            if h.val != r.val:
                return False
            # Recursively check left and right children
            return check(h.next, r.left) or check(h.next, r.right)

        if not root:
            return False

        # Iterative DFS to traverse every node in the tree as a potential starting point
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            # If the linked list starts at the current tree node, return True
            if check(head, node):
                return True
            # Push children to the stack to continue the search
            stack.append(node.left)
            stack.append(node.right)
            
        return False
# @lc code=end