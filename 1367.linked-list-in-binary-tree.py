#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
            if not head:
                return True  # Finished traversing the entire linked list
            if not node:
                return False  # Reached a leaf node without matching entire list
            if head.val == node.val:
                # Check either left or right subtree can continue matching
                return dfs(head.next, node.left) or dfs(head.next, node.right)
            return False  # Current values don't match; can't continue this path
        if not root:
            return False  # If root is null, no path can exist
        # Start DFS from current node or try from children (left/right) of current root
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
# @lc code=end