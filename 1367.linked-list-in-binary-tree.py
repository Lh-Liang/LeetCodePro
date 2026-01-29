#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, root):
            if not head:  # If head is None, we've matched all nodes of linked list
                return True
            if not root:  # If root is None, we've reached leaf without matching all nodes
                return False
            if head.val == root.val:  # Current nodes match, move to next nodes in both structures
                return dfs(head.next, root.left) or dfs(head.next, root.right)
            return False  # If values don't match, can't continue this path
        
        def traverse(root):
            if not root:  # Base case for traversal. No more nodes left in tree.
                return False
            return dfs(head, root) or traverse(root.left) or traverse(root.right)  # Check current node or move to children nodes
        
        return traverse(root)  # Start traversal from root of the tree
# @lc code=end