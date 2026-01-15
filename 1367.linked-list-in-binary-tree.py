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
        # Cache for memoization
        cache = {}
        
        def match(list_node: Optional[ListNode], tree_node: Optional[TreeNode]) -> bool:
            # If linked list is exhausted -> success
            if not list_node:
                return True
            # If binary tree node doesn't exist -> failure
            if not tree_node:
                return False
            
            # Check cache using object ids
            key = (id(list_node), id(tree_node))
            if key in cache:
                return cache[key]
            
            # Values don't match -> failure
            if list_node.val != tree_node.val:
                cache[key] = False
                return False
            
            # Try continuing down left or right subtree
            res = match(list_node.next, tree_node.left) or match(list_node.next, tree_node.right)
            cache[key] = res
            return res
        
        # Iterative DFS traversal of binary tree
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            # Check if path starts at current node
            if match(head, node):
                return True
            # Push children to stack
            stack.append(node.left)
            stack.append(node.right)
        
        # No matching path found
        return False
# @lc code=end