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
        def dfs(tree_node, list_node):
            if not list_node:
                return True  # Entire list matched.
            if not tree_node:
                return False  # Reached end of tree branch without full match.
            if tree_node.val == list_node.val:
                # Check both subtrees if they continue matching the remaining list.
                return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)
            return False  # Current path does not match.
        
        def traverse(tree):
            if not tree:
                return False  # No further nodes to check.
            # Start DFS from current node or proceed with left/right child nodes.
            return dfs(tree, head) or traverse(tree.left) or traverse(tree.right)
        
        return traverse(root)
# @lc code=end