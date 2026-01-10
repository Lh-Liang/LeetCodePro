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
        
        # Use iterative DFS to traverse the tree and find potential starting nodes.
        # This prevents reaching the recursion limit for trees with many nodes (up to 2500).
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            
            # If current node could be the start of the path, check it.
            if self.checkPath(head, node):
                return True
            
            # Add children to stack to continue searching for the start of the list.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return False

    def checkPath(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        # If we reached the end of the linked list, the path exists.
        if not head:
            return True
        # If the tree ends before the list, the path doesn't exist.
        if not node:
            return False
        # If values don't match, this path is invalid.
        if head.val != node.val:
            return False
        
        # Recursively check the left and right subtrees for the next list node.
        return self.checkPath(head.next, node.left) or self.checkPath(head.next, node.right)
# @lc code=end